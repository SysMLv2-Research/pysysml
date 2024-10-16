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
