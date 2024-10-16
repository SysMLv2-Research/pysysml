import pathlib
from typing import List, Optional

from lark import Lark

from .base import _grammar_file
from pysysml.utils import list_rules_from_grammar


def open_kerml_lark_parser(start: Optional[List[str]] = None) -> Lark:
    grammar_code = pathlib.Path(_grammar_file).read_text()
    rules = list_rules_from_grammar(grammar_code=grammar_code, show_alias=False)
    starts = rules
    starts.extend(list(start or []))
    starts = sorted(set(starts))
    return Lark.open(grammar_filename=_grammar_file, start=starts)
