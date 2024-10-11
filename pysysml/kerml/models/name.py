import re
from dataclasses import dataclass
from typing import List


def name_unescape(name: str):
    if name.startswith('\''):
        return eval(name)
    else:
        return name


def name_escape(name: str):
    return repr(name)


def name_safe_repr(name: str):
    if re.fullmatch(r'^[a-zA-Z_][a-zA-Z\d_]*$', name):
        return name
    else:
        return name_escape(name)


@dataclass
class QualifiedName:
    names: List[str]

    @property
    def repr(self):
        return '::'.join(map(name_safe_repr, self.names))
