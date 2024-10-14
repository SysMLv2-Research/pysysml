import os.path
import re
from functools import lru_cache
from typing import List, Set

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
    if not os.path.exists(_reserved_words_file):
        raise FileNotFoundError(f'Reserved words file for KerML not found - {_reserved_words_file!r}.')
    if not os.path.isfile(_reserved_words_file):
        raise IsADirectoryError(f'Reserved words file for KerML is not a file - {_reserved_words_file!r}.')
    if not os.path.exists(_grammar_file):
        raise FileNotFoundError(f'Grammar lark file for KerML not found - {_reserved_words_file!r}.')
    if not os.path.isfile(_grammar_file):
        raise IsADirectoryError(f'Grammar lark file for KerML not found - {_reserved_words_file!r}.')
