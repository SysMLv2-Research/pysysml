from dataclasses import dataclass

from .name import QualifiedName


@dataclass
class NullValue:
    @property
    def value(self):
        return None


@dataclass
class MetadataAccessExpression:
    qualified_name: QualifiedName
