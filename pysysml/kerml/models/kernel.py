from dataclasses import dataclass
from enum import unique, Enum
from typing import Optional, Union, List, Any

from .core import Classifier, FeatureDirection, FeatureRelationshipType, FeatureSpecializationPart, ConjugationPart, \
    FeatureRelationshipPart, FeatureValueType, Feature
from .glob import MultiplicityBounds, PrefixMetadataAnnotation
from .name import QualifiedName, FeatureChain, Identification
from .root import VisibleMember


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


@dataclass
class Succession:
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

    is_all_succession: bool
    first: Optional[ConnectorEnd]
    then: Optional[ConnectorEnd]

    body: List[Any]


@dataclass
class Behavior(Classifier):
    pass


@dataclass
class Step(Feature):
    pass


@dataclass
class Return(VisibleMember):
    feature: Feature


@dataclass
class Result(VisibleMember):
    expression: Any


@dataclass
class Function(Behavior):
    pass


@dataclass
class Expression(Step):
    pass


@dataclass
class Predicate(Function):
    pass


@dataclass
class BooleanExpression(Expression):
    pass


@dataclass
class Invariant(BooleanExpression):
    asserted: Optional[bool]


@dataclass
class IndexExpression:
    entity: Any
    sequence: List[Any]


@dataclass
class SequenceExpression:
    sequence: List[Any]


@dataclass
class FeatureChainExpression:
    entity: Any
    member: Union[QualifiedName, FeatureChain]


@dataclass
class CollectExpression:
    entity: Any
    body: List[Any]


@dataclass
class SelectExpression:
    entity: Any
    body: List[Any]


@dataclass
class BodyExpression:
    body: List[Any]


@dataclass
class FunctionOperationExpression:
    entity: Any
    name: QualifiedName
    arguments: List[Any]


@dataclass
class Interaction(Behavior):
    pass


@dataclass
class ItemFlowEnd:
    owned: Optional[Union[QualifiedName, FeatureChain]]
    member: QualifiedName


@dataclass
class ItemFeature:
    identification: Optional[Identification]
    specializations: List[FeatureSpecializationPart]
    multiplicity: Optional[MultiplicityBounds]
    is_ordered: bool
    is_nonunique: bool
    feature_typing: Optional[Union[QualifiedName, FeatureChain]]

    is_default: bool
    value_type: Optional[FeatureValueType]
    value: Optional[Any]


@dataclass
class ItemFlow:
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

    is_all_flow: bool
    end_from: Optional[ItemFlowEnd]
    end_to: Optional[ItemFlowEnd]
    item_feature: Optional[ItemFeature]

    body: List[Any]


@dataclass
class SuccessionItemFlow(ItemFlow):
    pass


@dataclass
class MultiplicitySubset:
    identification: Identification
    superset: Union[QualifiedName, FeatureChain]
    body: List[Any]


@dataclass
class MultiplicityRange:
    identification: Identification
    multiplicity: MultiplicityBounds
    body: List[Any]


@dataclass
class Metaclass(Struct):
    pass


@dataclass
class Metadata:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    superclass: Optional[Union[QualifiedName, FeatureChain]]
    about: List[Union[QualifiedName, FeatureChain]]
    body: List[Any]


@dataclass
class MetadataRedefine:
    name: Union[QualifiedName, FeatureChain]

    specializations: List[FeatureSpecializationPart]
    multiplicity: Optional[MultiplicityBounds]
    is_ordered: bool
    is_nonunique: bool

    is_default: bool
    value_type: Optional[FeatureValueType]
    value: Optional[Any]

    body: List[Any]


@dataclass
class ElementFilter(VisibleMember):
    expression: Any


@dataclass
class Package:
    annotations: List[PrefixMetadataAnnotation]
    identification: Identification
    body: List[Any]


@dataclass
class LibraryPackage(Package):
    is_standard: bool


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
