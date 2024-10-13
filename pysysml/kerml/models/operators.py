from dataclasses import dataclass
from typing import Any, Optional

from pysysml.kerml.models import QualifiedName


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


@dataclass
class ClsTestOp:
    op: str
    x: Optional[Any]
    y: QualifiedName


@dataclass
class ClsCastOp:
    x: Optional[Any]
    y: QualifiedName


@dataclass
class MetaClsTestOp:
    op: str
    x: Optional[Any]
    y: QualifiedName


@dataclass
class MetaClsCastOp:
    x: Optional[Any]
    y: QualifiedName
