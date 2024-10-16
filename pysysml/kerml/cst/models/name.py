import dataclasses
import re
from dataclasses import dataclass
from typing import List, Optional


def name_unescape(name: str):
    if name.startswith('\''):
        return eval(name)
    else:
        return name


def name_escape(name: str):
    return repr(name)


def name_safe_repr(name: str):
    if re.fullmatch(r'^[a-zA-Z_][a-zA-Z\d_]*$', name):
        return name
    else:
        return name_escape(name)


@dataclass
class QualifiedName:
    names: List[str]

    @property
    def repr(self):
        return '::'.join(map(name_safe_repr, self.names))

    def _value(self):
        return tuple(self.names)

    def __hash__(self):
        return hash(self._value())

    def __eq__(self, other):
        return isinstance(other, QualifiedName) and self._value() == other._value()


@dataclass
class Identification:
    short_name: Optional[str]
    name: Optional[str]

    def __bool__(self):
        return bool(self.short_name is not None or self.name is not None)


@dataclasses.dataclass
class FeatureChain:
    items: List[QualifiedName]

    @property
    def repr(self):
        return '.'.join(map(lambda x: x.repr, self.items))

    def _value(self):
        return tuple(self.items)

    def __hash__(self):
        return hash(self._value())

    def __eq__(self, other):
        return isinstance(other, FeatureChain) and self._value() == other._value()
