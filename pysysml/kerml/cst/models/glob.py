from dataclasses import dataclass
from enum import unique, Enum
from typing import Optional, Union

from .literal import LiteralValue
from .name import QualifiedName, FeatureChain


@dataclass
class MultiplicityBounds:
    lower_bound: Optional[Union[LiteralValue, QualifiedName]]
    upper_bound: Union[LiteralValue, QualifiedName]


@unique
class Visibility(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'

    @classmethod
    def load(cls, v: str) -> 'Visibility':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'


@dataclass
class PrefixMetadataAnnotation:
    feature: Union[QualifiedName, FeatureChain]
