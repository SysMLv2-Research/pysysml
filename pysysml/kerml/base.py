import os.path
import re
from functools import lru_cache
from typing import List, Set

from ..utils import file_health_check

_reserved_words_file = os.path.normpath(os.path.join(__file__, '..', 'reserved_words.txt'))
_grammar_file = os.path.normpath(os.path.join(__file__, '..', 'syntax.lark'))


@lru_cache()
def list_reserved_words() -> List[str]:
    with open(_reserved_words_file, 'r') as f:
        return list(filter(bool, re.split(r'\s+', f.read())))


@lru_cache()
def _reserved_words_set() -> Set[str]:
    return set(list_reserved_words())


def is_reserved_word(word: str) -> bool:
    return word in _reserved_words_set()


def resource_file_check():
    file_health_check(_reserved_words_file)
    file_health_check(_grammar_file)
