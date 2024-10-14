from dataclasses import dataclass
from typing import List, Optional, Any

from . import PrefixMetadataAnnotation
from .glob import Visibility
from .name import Identification, QualifiedName


@dataclass
class Dependency:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    from_list: List[QualifiedName]
    to_list: List[QualifiedName]
    body: List[Any]


@dataclass
class IRegularComment:
    comment: str


@dataclass
class Comment(IRegularComment):
    identification: Optional[Identification]
    about_list: Optional[List[QualifiedName]]
    locale: Optional[str]


@dataclass
class Documentation(IRegularComment):
    identification: Identification
    locale: Optional[str]


@dataclass
class TextualRepresentation(IRegularComment):
    identification: Optional[Identification]
    language: str


@dataclass
class RelationshipBody:
    elements: List[Any]


@dataclass
class Namespace:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    body: List[Any]


@dataclass
class RootNamespace:
    body: List[Any]


@dataclass
class VisibleMember:
    visibility: Optional[Visibility]


@dataclass
class NonFeatureMember(VisibleMember):
    element: Any


@dataclass
class OwnedFeatureMember(VisibleMember):
    element: Any


@dataclass
class TypeFeatureMember(VisibleMember):
    element: Any


@dataclass
class NamespaceFeatureMember(VisibleMember):
    element: Any


@dataclass
class Import(VisibleMember):
    is_all: bool
    is_recursive: bool
    is_namespace: bool
    name: QualifiedName
    filters: List[Any]
    body: List[Any]


@dataclass
class Alias(VisibleMember):
    identification: Identification
    name: QualifiedName
    body: List[Any]
