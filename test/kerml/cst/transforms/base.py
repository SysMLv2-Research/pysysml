from functools import lru_cache

from pysysml.kerml.cst import open_kerml_lark_parser, tree_to_kerml_cst, KerMLTransRecorder


@lru_cache()
def _parser_for_rule(rule_name, no_previous_starts: bool = False):
    lark = open_kerml_lark_parser(start=[rule_name])

    def _parse(x):
        tree = lark.parse(x, start=rule_name)
        recorder = KerMLTransRecorder()
        recorder.transform(tree)
        return tree_to_kerml_cst(tree), recorder.rules

    return _parse
