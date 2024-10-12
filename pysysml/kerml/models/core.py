from dataclasses import dataclass
from enum import unique, Enum
from typing import List, Union, Optional, Any

from .feature import FeatureChain
from .kernel import MultiplicityBounds
from .metadata import PrefixMetadataAnnotation
from .name import QualifiedName, Identification


@dataclass
class SuperclassingPart:
    items: List[QualifiedName]


@dataclass
class SpecializationPart:
    items: List[QualifiedName]


@dataclass
class ConjugationPart:
    item: Union[FeatureChain, QualifiedName]


@dataclass
class DisjoiningPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class UnioningPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class IntersectingPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class DifferencingPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class Class:
    is_abstract: bool
    annotations: List[PrefixMetadataAnnotation]
    is_all: bool
    identification: Identification
    multiplicity_bounds: Optional[MultiplicityBounds]
    conjugation: Optional[ConjugationPart]
    superclassing: Optional[SuperclassingPart]
    relationships: List[Union[DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart]]
    body: List[Any]


@dataclass
class Type:
    is_abstract: bool
    annotations: List[PrefixMetadataAnnotation]
    is_all: bool
    identification: Identification
    multiplicity_bounds: Optional[MultiplicityBounds]
    conjugation: Optional[ConjugationPart]
    specialization: Optional[SpecializationPart]
    relationships: List[Union[DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart]]
    body: List[Any]


@dataclass
class ChainingPart:
    item: Union[FeatureChain, QualifiedName]


@dataclass
class InvertingPart:
    item: Union[FeatureChain, QualifiedName]


@dataclass
class TypeFeaturingPart:
    items: List[QualifiedName]


@dataclass
class TypingsPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class SubsettingsPart:
    items: List[Union[FeatureChain, QualifiedName]]


@dataclass
class ReferencesPart:
    item: Union[FeatureChain, QualifiedName]


@dataclass
class RedefinitionsPart:
    items: List[Union[FeatureChain, QualifiedName]]


TypeRelationshipPart = Union[DisjoiningPart, UnioningPart, IntersectingPart, DifferencingPart]
FeatureRelationshipPart = Union[TypeRelationshipPart, ChainingPart, InvertingPart, TypeFeaturingPart]
FeatureSpecializationPart = Union[TypingsPart, SubsettingsPart, ReferencesPart, RedefinitionsPart]


@unique
class FeatureDirection(Enum):
    IN = 'in'
    OUT = 'out'
    INOUT = 'inout'

    @classmethod
    def load(cls, v: str) -> 'FeatureDirection':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'


@unique
class FeatureRelationshipType(Enum):
    COMPOSITE = 'composite'
    PORTION = 'portion'

    @classmethod
    def load(cls, v: str) -> 'FeatureRelationshipType':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'


@unique
class FeatureValueType(Enum):
    BIND = 'bind'
    INITIAL = 'initial'

    @classmethod
    def load(cls, v: str) -> 'FeatureValueType':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'


@dataclass
class Feature:
    direction: Optional[FeatureDirection]
    is_abstract: bool
    relationship_type: Optional[FeatureRelationshipType]
    is_readonly: bool
    is_derived: bool
    is_end: bool
    annotations: List[PrefixMetadataAnnotation]

    is_all: bool
    identification: Optional[Identification]
    specializations: List[FeatureSpecializationPart]
    multiplicity: Optional[MultiplicityBounds]
    is_ordered: bool
    is_nonunique: bool
    conjugation: Optional[ConjugationPart]
    relationships: List[FeatureRelationshipPart]

    is_default: bool
    value_type: Optional[FeatureValueType]
    value: Optional[Any]

    body: List[Any]
