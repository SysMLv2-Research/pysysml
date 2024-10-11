import json
import math
from dataclasses import dataclass


@dataclass
class IntValue:
    raw: str

    @property
    def value(self) -> int:
        return int(self.raw.lstrip('0') or '0')


@dataclass
class RealValue:
    raw: str

    @property
    def value(self) -> float:
        return float(self.raw)


@dataclass
class BoolValue:
    raw: str

    @property
    def value(self) -> bool:
        return self.raw.lower() == 'true'


@dataclass
class StringValue:
    raw: str

    @property
    def value(self) -> str:
        return json.loads(self.raw)


@dataclass
class InfValue:
    raw: str

    @property
    def value(self) -> float:
        return math.inf
