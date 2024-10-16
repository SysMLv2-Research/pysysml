from dataclasses import dataclass
from enum import unique, Enum
from typing import List, Union, Optional, Any

from .glob import MultiplicityBounds, PrefixMetadataAnnotation
from .name import QualifiedName, Identification, FeatureChain


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
class GenericFeature:
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

    body: List[Any]


@dataclass
class Feature(GenericFeature):
    is_default: bool
    value_type: Optional[FeatureValueType]
    value: Optional[Any]


@dataclass
class Specialization:
    identification: Optional[Identification]
    specific_type: Union[QualifiedName, FeatureChain]
    general_type: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class Conjugation:
    identification: Optional[Identification]
    conjugate_type: Union[QualifiedName, FeatureChain]
    conjugated_type: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class Disjoining:
    identification: Optional[Identification]
    disjoint_type: Union[QualifiedName, FeatureChain]
    separated_type: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class Classifier:
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
class Subclassification:
    identification: Optional[Identification]
    subclassifier: QualifiedName
    superclassifier: QualifiedName
    body: List[Any]


@dataclass
class FeatureTyping:
    identification: Optional[Identification]
    typed_entity: QualifiedName
    typing_type: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class Subsetting:
    identification: Optional[Identification]
    subset: Union[QualifiedName, FeatureChain]
    superset: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class Redefinition:
    identification: Optional[Identification]
    entity: Union[QualifiedName, FeatureChain]
    redefined_to: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class FeatureInverting:
    identification: Optional[Identification]
    inverted: Union[QualifiedName, FeatureChain]
    target: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class TypeFeaturing:
    identification: Optional[Identification]
    featured_entity: Union[QualifiedName, FeatureChain]
    feature_provider: Union[QualifiedName, FeatureChain]
    body: List[Any]
