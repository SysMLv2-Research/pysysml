from dataclasses import dataclass
from typing import Any


@dataclass
class ExtentOp:
    x: Any


@dataclass
class UnaryOp:
    op: str
    x: Any


@dataclass
class BinOp:
    op: str
    x: Any
    y: Any


@dataclass
class CondBinOp:
    op: str
    x: Any
    y: Any


@dataclass
class IfTestOp:
    condition: Any
    if_true: Any
    if_false: Any
