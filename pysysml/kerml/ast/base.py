import uuid
import weakref
from abc import ABC
from collections.abc import MutableSequence, Sequence, Sized
from typing import Dict, List, Union, Optional, Iterator, TypeVar, Generic, Iterable, Type, Callable

from hbutils.string import plural_word
from ordered_set import OrderedSet


class ElementNotFoundError(Exception):
    def __init__(self, env, key):
        Exception.__init__(self, f'Element {key!r} not found in env {env!r}.', (env, key))
        self.env = env
        self.key = key


T = TypeVar('T', bound='IElementID')


class Env(Sized, Generic[T]):
    def __init__(self):
        self._elements: Dict[str, T] = {}

    def __getitem__(self, key: Union[str, T]) -> T:
        if isinstance(key, IElementID):
            key = key.element_id
        if key in self._elements:
            return self._elements[key]
        else:
            raise ElementNotFoundError(self, key)

    def __setitem__(self, key: Union[str, T], value: T):
        if isinstance(key, IElementID):
            key = key.element_id
        if isinstance(value, IElementID):
            self._elements[key] = value
        else:
            raise TypeError(f'Element should be IElementID, but {value!r} given.')

    def __delitem__(self, key: Union[str, T]):
        if isinstance(key, IElementID):
            key = key.element_id
        del self._elements[key]

    def __contains__(self, key: Union[str, T]):
        if isinstance(key, IElementID):
            key = key.element_id
        return key in self._elements

    def __len__(self):
        return len(self._elements)

    def add(self, element: T):
        self[element] = element

    def __repr__(self):
        return f'<{self.__class__.__name__} {hex(id(self))}, {plural_word(len(self._elements), "item")}>'


class ConstraintsError(Exception):
    pass


class IElementID(ABC):
    def __init__(self, env: Env, element_id: Optional[str] = None):
        self._env_ref = weakref.ref(env)
        self._element_id: str = element_id if element_id else str(uuid.uuid4())
        self.env[self._element_id] = self

    @property
    def env(self) -> Env:
        return self._env_ref()

    @property
    def element_id(self) -> str:
        return self._element_id


def _to_element_id(value: Union[str, IElementID]) -> str:
    return value.element_id if isinstance(value, IElementID) else value


class _AbstractEList(ABC, Generic[T], Sequence, Sized):
    def __init__(self, env: Env, initial_elements: Optional[List[Union[str, T]]] = None):
        self._env = env
        self._elements: List[str] = [_to_element_id(v) for v in (initial_elements or [])]

    def _to_ielement(self, element_id: str) -> T:
        return self._env[element_id]

    def __getitem__(self, index: Union[int, slice]) -> Union[T, '_AbstractEList[T]']:
        result = self._elements[index]
        if isinstance(result, list):
            return self.__class__(env=self._env, initial_elements=result)
        else:
            return self._to_ielement(result)

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self) -> Iterator[T]:
        return (self._to_ielement(element_id) for element_id in self._elements)

    def __contains__(self, value: Union[str, T]) -> bool:
        return _to_element_id(value) in self._elements

    def index(self, value: Union[str, T], start: int = 0, stop: Optional[int] = None) -> int:
        return self._elements.index(_to_element_id(value), *((start, stop) if stop is not None else (start,)))

    def count(self, value: Union[str, T]) -> int:
        return self._elements.count(_to_element_id(value))

    def __repr__(self):
        return f"{self.__class__.__name__}({[self._to_ielement(item) for item in self._elements]})"

    def __eq__(self, other):
        return len(self) == len(other) and all(x == y for x, y in zip(self, other))


class EFrozenList(_AbstractEList, Generic[T]):
    def __init__(self, env: Env, initial_elements: Optional[List[Union[str, T]]] = None):
        _AbstractEList.__init__(self, env, initial_elements)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, 'EFrozenList[T]']:
        return _AbstractEList.__getitem__(self, index)

    def __len__(self) -> int:
        return _AbstractEList.__len__(self)

    def __iter__(self) -> Iterator[T]:
        yield from _AbstractEList.__iter__(self)

    def __contains__(self, value: Union[str, T]) -> bool:
        return _AbstractEList.__contains__(self, value)

    def index(self, value: Union[str, T], start: int = 0, stop: Optional[int] = None) -> int:
        return _AbstractEList.index(self, value, start, stop)

    def count(self, value: Union[str, T]) -> int:
        return _AbstractEList.count(self, value)


class EList(_AbstractEList, Generic[T], MutableSequence):
    def __init__(self, env: Env, initial_elements: Optional[List[Union[str, T]]] = None):
        _AbstractEList.__init__(self, env, initial_elements)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, 'EList[T]']:
        return _AbstractEList.__getitem__(self, index)

    def __setitem__(self, index: Union[int, slice], value: Union[str, T, List[Union[str, T]]]):
        if isinstance(index, slice):
            self._elements[index] = [_to_element_id(v) for v in value]
        else:
            self._elements[index] = _to_element_id(value)

    def __delitem__(self, index: Union[int, slice]):
        del self._elements[index]

    def __len__(self) -> int:
        return _AbstractEList.__len__(self)

    def __iter__(self) -> Iterator[T]:
        yield from _AbstractEList.__iter__(self)

    def __contains__(self, value: Union[str, T]) -> bool:
        return _AbstractEList.__contains__(self, value)

    def insert(self, index: int, value: Union[str, T]):
        self._elements.insert(index, _to_element_id(value))

    def append(self, value: Union[str, T]):
        self._elements.append(_to_element_id(value))

    def extend(self, values: List[Union[str, T]]):
        self._elements.extend(_to_element_id(v) for v in values)

    def index(self, value: Union[str, T], start: int = 0, stop: Optional[int] = None) -> int:
        return _AbstractEList.index(self, value, start, stop)

    def count(self, value: Union[str, T]) -> int:
        return _AbstractEList.count(self, value)


_AddConjFuncTyping = Callable[[T], None]
_RemoveConjFuncTyping = Callable[[T], None]


class EConn(Generic[T]):
    def __init__(self, env: Env, type_: Type[T] = IElementID, initial: Optional[Iterable[Union[str, T]]] = None,
                 fn_add_conj: Optional[_AddConjFuncTyping] = None,
                 fn_remove_conj: Optional[_RemoveConjFuncTyping] = None):
        self._env_ref = weakref.ref(env)
        self._type: Type[T] = type_
        self._set = OrderedSet()
        self._fn_add_conj = fn_add_conj
        self._fn_remove_conj = fn_remove_conj

        for element in (initial or []):
            self.add(element)

    @property
    def env(self) -> Env:
        return self._env_ref()

    def _to_ielement(self, element_id: str) -> T:
        return self.env[element_id]

    def __len__(self) -> int:
        return len(self._set)

    def __iter__(self) -> Iterator[T]:
        yield from (self._to_ielement(idx) for idx in self._set)

    def __contains__(self, value: Union[str, T]) -> bool:
        return _to_element_id(value) in self._set

    def add(self, value: Union[T, str], no_conj: bool = False) -> 'EConn[T]':
        element_id = _to_element_id(value)
        element = self.env[element_id]
        if not isinstance(element, self._type):
            raise TypeError(f'Element type {self._type!r} expected, but {element!r} found.')
        else:
            self._set.add(element_id)
        if not no_conj and self._fn_add_conj:
            self._fn_add_conj(element)
        return self

    def update(self, values: Iterable[Union[T, str]], no_conj: bool = False) -> 'EConn[T]':
        for item in values:
            self.add(item, no_conj=no_conj)
        return self

    def remove(self, value: Union[T, str], no_conj: bool = False) -> 'EConn[T]':
        element_id = _to_element_id(value)
        element = self.env[element_id]
        self._set.remove(element_id)
        if not no_conj and self._fn_remove_conj:
            self._fn_remove_conj(element)
        return self

    def clear(self, no_conj: bool = False):
        for element in list(self._set):
            self.remove(element, no_conj=no_conj)
        return self

    def first(self) -> Optional[T]:
        for element_id in self._set:
            return self._to_ielement(element_id)
        return None

    def set_to(self, element: Union[str, T], no_conj: bool = False):
        element_id = _to_element_id(element)
        element = self.env[element_id]
        self.clear(no_conj=no_conj)
        self.add(element, no_conj=no_conj)
        return self
