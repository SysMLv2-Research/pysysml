import os.path
from typing import List

import lark
from lark import Visitor, Tree


class LarkRuleVisitor(Visitor):
    def __init__(self):
        self._rule_set = set()
        self.rule_names = []

    def _add_rule_name(self, name):
        name = str(name)
        if name not in self._rule_set:
            self._rule_set.add(name)
            self.rule_names.append(name)

    def alias(self, tree: Tree):
        assert len(tree.children) == 2
        if tree.children[-1] is not None:
            self._add_rule_name(tree.children[-1])

    def rule(self, tree: Tree):
        self._add_rule_name(tree.children[0])


def list_rules_from_grammar(grammar_code: str, show_inner: bool = False, show_conditional: bool = False,
                            show_pinned: bool = True) -> List[str]:
    lark_grammar_file = os.path.normpath(os.path.join(lark.__file__, '..', 'grammars', 'lark.lark'))
    parser = lark.Lark.open(lark_grammar_file, rel_to=__file__, parser="lalr")
    ast = parser.parse(grammar_code)

    visitor = LarkRuleVisitor()
    visitor.visit(ast)
    result = []
    for rule_name in visitor.rule_names:
        if rule_name.startswith('!'):
            is_pinned = True
            rule_name = rule_name[1:]
        else:
            is_pinned = False
        is_inner, is_conditional = False, False
        if rule_name.startswith('_') or rule_name.startswith('?'):
            if rule_name.startswith('_'):
                is_inner = True
            elif rule_name.startswith('?'):
                is_conditional = True
            else:
                assert False, 'Should not reach this line!'  # pragma: no cover
            rule_name = rule_name[1:]

        if (not is_pinned or show_pinned) and (not is_inner or show_inner) and (not is_conditional or show_conditional):
            result.append(rule_name)

    return result
