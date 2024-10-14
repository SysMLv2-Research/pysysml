import os
import pathlib
from typing import List, Optional

from lark import Lark

from pysysml import __file__ as _pysysml_file
from pysysml.utils import list_rules_from_grammar

_grammar_file = os.path.normpath(os.path.join(__file__, '..', 'demo.lark'))


def open_demo_lark_parser(start: Optional[List[str]] = None) -> Lark:
    grammar_code = pathlib.Path(_grammar_file).read_text()
    rules = list_rules_from_grammar(grammar_code=grammar_code, show_alias=False)
    starts = rules
    starts.extend(list(start or []))
    starts = sorted(set(starts))
    return Lark.open(
        grammar_filename=_grammar_file,
        start=starts,
        import_paths=[
            os.path.normpath(os.path.join(__file__, '..')),
            os.path.normpath(os.path.join(_pysysml_file, '..')),
        ]
    )
