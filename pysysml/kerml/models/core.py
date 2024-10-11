from dataclasses import dataclass
from typing import List, Union, Optional, Any

from .feature import FeatureChain
from .kernel import MultiplicityBounds
from .metadata import PrefixMetadataAnnotation
from .name import QualifiedName, Identification


@dataclass
class SuperclassingPart:
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
