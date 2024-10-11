from dataclasses import dataclass
from typing import Optional, Union

from .literal_expression import LiteralValue
from .name import QualifiedName


@dataclass
class MultiplicityBounds:
    lower_bound: Optional[Union[LiteralValue, QualifiedName]]
    upper_bound: Union[LiteralValue, QualifiedName]
