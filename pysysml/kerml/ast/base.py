import uuid
from typing import Dict, Any, Optional


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


class IElementID:
    def __init__(self, env: Env, element_id: Optional[str] = None):
        self._env = env
        self.element_id: str = element_id if element_id else str(uuid.uuid4())
        self._env[self.element_id] = self

    def __del__(self):
        if self.element_id in self._env:
            del self._env[self.element_id]


from typing import List, Union, Optional, Iterator
from collections.abc import MutableSequence


class Sequence(MutableSequence):
    def __init__(self, env: Env, initial_elements: Optional[List[Union[str, IElementID]]] = None):
        self._env = env
        self._elements: List[str] = []
        if initial_elements:
            self.extend(initial_elements)

    def _to_element_id(self, value: Union[str, IElementID]) -> str:
        return value.element_id if isinstance(value, IElementID) else value

    def _to_ielement(self, element_id: str) -> IElementID:
        return self._env[element_id]

    def __getitem__(self, index: Union[int, slice]) -> Union[IElementID, List[IElementID]]:
        if isinstance(index, slice):
            return [self._to_ielement(element_id) for element_id in self._elements[index]]
        return self._to_ielement(self._elements[index])

    def __setitem__(self, index: Union[int, slice], value: Union[str, IElementID, List[Union[str, IElementID]]]):
        if isinstance(index, slice):
            self._elements[index] = [self._to_element_id(v) for v in value]
        else:
            self._elements[index] = self._to_element_id(value)

    def __delitem__(self, index: Union[int, slice]):
        del self._elements[index]

    def __len__(self) -> int:
        return len(self._elements)

    def insert(self, index: int, value: Union[str, IElementID]):
        self._elements.insert(index, self._to_element_id(value))

    def append(self, value: Union[str, IElementID]):
        self._elements.append(self._to_element_id(value))

    def extend(self, values: List[Union[str, IElementID]]):
        self._elements.extend(self._to_element_id(v) for v in values)

    def __iter__(self) -> Iterator[IElementID]:
        return (self._to_ielement(element_id) for element_id in self._elements)

    def __contains__(self, value: Union[str, IElementID]) -> bool:
        return self._to_element_id(value) in self._elements

    def index(self, value: Union[str, IElementID], start: int = 0, stop: Optional[int] = None) -> int:
        return self._elements.index(self._to_element_id(value), start, stop)

    def count(self, value: Union[str, IElementID]) -> int:
        return self._elements.count(self._to_element_id(value))

    def remove(self, value: Union[str, IElementID]):
        self._elements.remove(self._to_element_id(value))

    def __repr__(self):
        return f"Sequence({self._elements})"
