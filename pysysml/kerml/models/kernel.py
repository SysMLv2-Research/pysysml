from dataclasses import dataclass
from enum import unique, Enum
from typing import Optional, Union, List, Any

from .core import Classifier, FeatureDirection, FeatureRelationshipType, FeatureSpecializationPart, ConjugationPart, \
    FeatureRelationshipPart, FeatureValueType
from .glob import MultiplicityBounds
from .metadata import PrefixMetadataAnnotation
from .name import QualifiedName, FeatureChain, Identification


@dataclass
class DataType(Classifier):
    pass


@dataclass
class Class(Classifier):
    pass


@dataclass
class Struct(Classifier):
    pass


@dataclass
class Association(Classifier):
    pass


@dataclass
class AssociationStruct(Classifier):
    pass


@dataclass
class ConnectorEnd:
    name: Optional[str]
    reference: Union[QualifiedName, FeatureChain]
    multiplicity: Optional[MultiplicityBounds]


@unique
class ConnectorType(Enum):
    VALUE = 'value'
    BINARY = 'binary'
    NARY = 'nary'

    @classmethod
    def load(cls, v: str) -> 'ConnectorType':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'


@dataclass
class Connector:
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

    type: ConnectorType

    is_default: bool
    value_type: Optional[FeatureValueType]
    value: Optional[Any]

    is_all_connect: bool
    ends: Optional[List[ConnectorEnd]]

    body: List[Any]


@dataclass
class BindingConnector:
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

    is_all_binding: bool
    bind_entity: Optional[ConnectorEnd]
    bind_to: Optional[ConnectorEnd]

    body: List[Any]
