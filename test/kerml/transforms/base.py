from functools import lru_cache

from pysysml.kerml import open_kerml_lark_parser
from pysysml.kerml.transforms import tree_to_cst, KerMLTransRecorder


@lru_cache()
def _parser_for_rule(rule_name):
    lark = open_kerml_lark_parser(start=[rule_name])

    def _parse(x):
        tree = lark.parse(x, start=rule_name)
        recorder = KerMLTransRecorder()
        recorder.transform(tree)
        return tree_to_cst(tree), recorder.rules

    return _parse
