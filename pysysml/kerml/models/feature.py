import dataclasses
from typing import List

from .name import QualifiedName


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
