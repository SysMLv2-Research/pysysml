from dataclasses import dataclass
from typing import List, Optional, Any

from . import Visibility
from .metadata import PrefixMetadataAnnotation
from .name import Identification, QualifiedName


@dataclass
class Dependency:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    from_list: List[QualifiedName]
    to_list: List[QualifiedName]
    body: List[Any]


@dataclass
class Comment:
    identification: Optional[Identification]
    about_list: Optional[List[QualifiedName]]
    locale: Optional[str]
    comment: str


@dataclass
class Documentation:
    identification: Identification
    locale: Optional[str]
    comment: str


@dataclass
class TextualRepresentation:
    identification: Optional[Identification]
    language: str
    comment: str


@dataclass
class RelationshipBody:
    elements: List[Any]


@dataclass
class Namespace:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    body: List[Any]


@dataclass
class NonFeatureMember:
    visibility: Optional[Visibility]
    element: Any


@dataclass
class OwnedFeatureMember:
    visibility: Optional[Visibility]
    element: Any


@dataclass
class TypeFeatureMember:
    visibility: Optional[Visibility]
    element: Any


@dataclass
class NamespaceFeatureMember:
    visibility: Optional[Visibility]
    element: Any


@dataclass
class Import:
    visibility: Optional[Visibility]
    is_all: bool
    is_recursive: bool
    is_namespace: bool
    name: QualifiedName
    filters: List[Any]
    body: List[Any]
