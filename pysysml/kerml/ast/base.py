import uuid
from abc import ABC
from collections.abc import MutableSequence
from typing import Dict, Any, List, Union, Optional, Iterator, TypeVar, Generic, Sequence


class ElementNotFoundError(Exception):
    def __init__(self, env, key):
        Exception.__init__(self, f'Element {key!r} not found in env {env!r}.', (env, key))
        self.env = env
        self.key = key


class Env:
    def __init__(self, safe: bool = False):
        self._elements: Dict[str, Any] = {}
        self._safe: bool = safe

    @property
    def safe(self) -> bool:
        return self._safe

    def __getitem__(self, key):
        if isinstance(key, IElementID):
            key = key.element_id
        if key in self._elements:
            return self._elements[key]
        else:
            raise ElementNotFoundError(self, key)

    def __setitem__(self, key, value):
        if isinstance(key, IElementID):
            key = key.element_id
        self._elements[key] = value

    def __delitem__(self, key):
        if isinstance(key, IElementID):
            key = key.element_id
        del self._elements[key]

    def add(self, element: 'IElementID'):
        self[element.element_id] = element

    def __repr__(self):
        return f'<{self.__class__.__name__} {hex(id(self))}, safe: {self._safe!r}>'


class ConstraintsError(Exception):
    pass


class IElementID(ABC):
    def __init__(self, env: Env, element_id: Optional[str] = None):
        self._env = env
        self._element_id: str = element_id if element_id else str(uuid.uuid4())
        self._env[self._element_id] = self

    @property
    def element_id(self) -> str:
        return self._element_id

    def __del__(self):
        if self.element_id in self._env:
            del self._env[self._element_id]


def _to_element_id(value: Union[str, IElementID]) -> str:
    return value.element_id if isinstance(value, IElementID) else value


T = TypeVar('T', bound=IElementID)


class _AbstractEList(ABC, Generic[T], Sequence[T]):
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
            self._to_ielement(result)

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self) -> Iterator[T]:
        return (self._to_ielement(element_id) for element_id in self._elements)

    def __contains__(self, value: Union[str, T]) -> bool:
        return _to_element_id(value) in self._elements

    def index(self, value: Union[str, T], start: int = 0, stop: Optional[int] = None) -> int:
        return self._elements.index(_to_element_id(value), start, stop)

    def count(self, value: Union[str, T]) -> int:
        return self._elements.count(_to_element_id(value))

    def __repr__(self):
        return f"{self.__class__.__name__}({[self._to_ielement(item) for item in self._elements]})"


class EFrozenList(_AbstractEList):
    def __getitem__(self, index: Union[int, slice]) -> Union[T, 'EFrozenList[T]']:
        return _AbstractEList.__getitem__(self, index)


class EList(_AbstractEList, MutableSequence[T]):
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

    def insert(self, index: int, value: Union[str, T]):
        self._elements.insert(index, _to_element_id(value))

    def append(self, value: Union[str, T]):
        self._elements.append(_to_element_id(value))

    def extend(self, values: List[Union[str, T]]):
        self._elements.extend(_to_element_id(v) for v in values)
