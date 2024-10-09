import os.path
from typing import List

import lark
from lark import Visitor, Tree


class LarkRuleVisitor(Visitor):
    def __init__(self):
        self.rule_nodes: List[Tree] = []

    def rule(self, tree):
        self.rule_nodes.append(tree)


def list_rules_from_grammar(grammar_code: str) -> List[str]:
    lark_grammar_file = os.path.normpath(os.path.join(lark.__file__, '..', 'grammars', 'lark.lark'))
    parser = lark.Lark.open(lark_grammar_file, rel_to=__file__, parser="lalr")
    ast = parser.parse(grammar_code)

    visitor = LarkRuleVisitor()
    visitor.visit(ast)
    return [str(node.children[0]) for node in visitor.rule_nodes]
