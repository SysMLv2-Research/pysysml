from dataclasses import dataclass
from typing import List, Optional, Any

from .metadata import PrefixMetadataAnnotation
from .name import Identification, QualifiedName


@dataclass
class Dependency:
    annotations: List[PrefixMetadataAnnotation]
    identification: Optional[Identification]
    from_list: List[QualifiedName]
    to_list: List[QualifiedName]
    relationship_body: Any


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
