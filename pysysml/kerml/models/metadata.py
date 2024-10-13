from dataclasses import dataclass
from typing import Union

from .name import QualifiedName, FeatureChain


@dataclass
class PrefixMetadataAnnotation:
    feature: Union[QualifiedName, FeatureChain]
