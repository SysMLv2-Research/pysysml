from dataclasses import dataclass


@dataclass
class Name:
    symbol: str

    @property
    def is_restricted(self):
        return not self.symbol.startswith('\'')

    @property
    def translated(self):
        if self.is_restricted:
            return eval(self.symbol)
        else:
            return self.symbol
