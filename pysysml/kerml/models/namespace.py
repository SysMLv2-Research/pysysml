from enum import Enum, unique


@unique
class Visibility(Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'

    @classmethod
    def load(cls, v: str) -> 'Visibility':
        for name, value in cls.__members__.items():
            if v.upper() == name:
                return value

        raise ValueError(f'Unknown value for visibility - {v!r}.')

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'
