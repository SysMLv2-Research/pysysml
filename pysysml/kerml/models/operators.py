from dataclasses import dataclass
from typing import Any


@dataclass
class ExtentOp:
    x: Any


@dataclass
class UnaryOp:
    op: str
    x: Any
