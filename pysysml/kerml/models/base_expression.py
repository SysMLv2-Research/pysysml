from dataclasses import dataclass
from typing import Union, Any, List

from .name import QualifiedName, FeatureChain


@dataclass
class NullValue:
    @property
    def repr(self):
        return 'null'

    @property
    def value(self):
        return None


@dataclass
class MetadataAccessExpression:
    qualified_name: QualifiedName


@dataclass
class NamedArgument:
    name: QualifiedName
    value: Any  # TODO: use a proper typing schema


@dataclass
class InvocationExpression:
    name: Union[FeatureChain, QualifiedName]
    arguments: List[Any]

    # @property
    # def repr(self):
    #     return f'{self.repr}()'

    def _value(self):
        return self.name, tuple(self.arguments)

    def __hash__(self):
        return hash(self._value())

    def __eq__(self, other):
        return isinstance(other, InvocationExpression) and self._value() == other._value()
