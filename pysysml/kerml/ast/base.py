import uuid
import weakref
from abc import ABC
from collections.abc import Sized
from typing import Dict, Union, Optional, Iterator, TypeVar, Generic, Iterable, Type, Callable

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


_AddConjFuncTyping = Callable[[T], None]
_RemoveConjFuncTyping = Callable[[T], None]


class EConn(Generic[T]):
    def __init__(self, env: Env, type_: Type[T] = IElementID,
                 initial: Optional[Iterable[Union[str, T]]] = None,
                 no_conj_when_init: bool = False,
                 fn_add_conj: Optional[_AddConjFuncTyping] = None,
                 fn_remove_conj: Optional[_RemoveConjFuncTyping] = None):
        self._env_ref = weakref.ref(env)
        self._type: Type[T] = type_
        self._set = OrderedSet()
        self._fn_add_conj = fn_add_conj
        self._fn_remove_conj = fn_remove_conj

        for element in (initial or []):
            self.add(element, no_conj=no_conj_when_init)

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
            if element_id not in self._set:
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
        if element_id in self._set:
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
        for e in list(self._set):
            if e != element.element_id:
                self.remove(e, no_conj=no_conj)
        if element not in self:
            self.add(element, no_conj=no_conj)
        return self

    def is_subset(self, superset: Iterable[Union[str, T]]) -> bool:
        superset = {_to_element_id(e) for e in superset}
        return self._set.issubset(superset)

    def is_superset(self, subset: Iterable[Union[str, T]]) -> bool:
        subset = {_to_element_id(e) for e in subset}
        return self._set.issuperset(subset)

    def __bool__(self) -> bool:
        return bool(self._set)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({", ".join(map(repr, self))})'

    def __eq__(self, other) -> bool:
        return len(self) == len(other) and all(x == y for x, y in zip(self, other))
