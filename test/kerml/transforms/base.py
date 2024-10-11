from lark import Lark

from pysysml.kerml import __grammar_file__
from pysysml.kerml.transforms import tree_to_cst, KerMLTransRecorder


def _parser_for_rule(rule_name):
    lark = Lark.open(
        grammar_filename=__grammar_file__,
        start=[rule_name],
    )

    def _parse(x):
        tree = lark.parse(x, start=rule_name)
        recorder = KerMLTransRecorder()
        recorder.transform(tree)
        return tree_to_cst(tree), recorder.rules

    return _parse
