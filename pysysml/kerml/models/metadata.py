from dataclasses import dataclass
from typing import Union

from .feature import FeatureChain
from .name import QualifiedName


@dataclass
class PrefixMetadataAnnotation:
    feature: Union[QualifiedName, FeatureChain]
