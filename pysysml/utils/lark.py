import os.path
from typing import List, Dict

import lark
from lark import Visitor, Tree


class LarkRuleVisitor(Visitor):
    def __init__(self):
        self._rule_set = set()
        self.rule_dicts: Dict[str, List[str]] = {}

    def _add_rule_name(self, name, rule_type: str):
        name = str(name)
        if name not in self._rule_set:
            self._rule_set.add(name)
            if rule_type not in self.rule_dicts:
                self.rule_dicts[rule_type] = []
            self.rule_dicts[rule_type].append(name)

    def alias(self, tree: Tree):
        assert len(tree.children) == 2
        if tree.children[-1] is not None:
            self._add_rule_name(tree.children[-1], rule_type='alias')

    def rule(self, tree: Tree):
        self._add_rule_name(tree.children[0], rule_type='rule')


def list_rules_from_grammar(grammar_code: str, show_inner: bool = False, show_conditional: bool = False,
                            show_alias: bool = True, show_pinned: bool = True) -> List[str]:
    lark_grammar_file = os.path.normpath(os.path.join(lark.__file__, '..', 'grammars', 'lark.lark'))
    parser = lark.Lark.open(lark_grammar_file, rel_to=__file__, parser="lalr")
    ast = parser.parse(grammar_code)

    visitor = LarkRuleVisitor()
    visitor.visit(ast)
    result = []
    rule_names = visitor.rule_dicts.get('rule') or []
    if show_alias and 'alias' in visitor.rule_dicts:
        rule_names.extend(visitor.rule_dicts['alias'])
    for rule_name in rule_names:
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
