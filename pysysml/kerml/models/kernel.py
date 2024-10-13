from dataclasses import dataclass

from .core import Classifier


@dataclass
class DataType(Classifier):
    pass


@dataclass
class Class(Classifier):
    pass


@dataclass
class Struct(Classifier):
    pass


@dataclass
class Association(Classifier):
    pass


@dataclass
class AssociationStruct(Classifier):
    pass
