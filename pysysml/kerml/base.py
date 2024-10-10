import os.path
import re
from functools import lru_cache
from typing import List


@lru_cache()
def list_reserved_words() -> List[str]:
    with open(os.path.abspath(os.path.join(__file__, '..', 'reserved_words.txt')), 'r') as f:
        return list(filter(bool, re.split(r'\s+', f.read())))
