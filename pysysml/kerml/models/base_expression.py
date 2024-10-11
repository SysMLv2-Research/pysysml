from dataclasses import dataclass


@dataclass
class NullValue:
    @property
    def value(self):
        return None
