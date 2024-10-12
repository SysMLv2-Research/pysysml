import os.path

import lark
import pytest

from pysysml.utils import list_rules_from_grammar


@pytest.fixture()
def common_lark_file():
    return os.path.abspath(os.path.join(lark.__file__, '..', 'grammars', 'common.lark'))


@pytest.fixture()
def common_lark_code(common_lark_file):
    with open(common_lark_file, 'r') as f:
        return f.read()


@pytest.fixture()
def lark_lark_file():
    return os.path.abspath(os.path.join(lark.__file__, '..', 'grammars', 'lark.lark'))


@pytest.fixture()
def lark_lark_code(lark_lark_file):
    with open(lark_lark_file, 'r') as f:
        return f.read()


@pytest.mark.unittest
class TestUtilsLark:
    def test_list_rules_from_grammar_common(self, common_lark_code):
        assert list_rules_from_grammar(grammar_code=common_lark_code) == []

    def test_list_rules_from_grammar_lark(self, lark_lark_code):
        assert set(list_rules_from_grammar(grammar_code=lark_lark_code)) == \
               {
                   'ignore', 'import', 'multi_import', 'override_rule', 'declare', 'maybe', 'literal_range',
                   'literal', 'template_usage', 'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',
               }

    def test_list_rules_from_grammar_lark_inner(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_inner=True
        )) == {
                   'ignore', 'import', 'multi_import', 'override_rule', 'declare', 'maybe', 'literal_range',
                   'literal', 'template_usage', 'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'item',
               }

    def test_list_rules_from_grammar_lark_conditional(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_conditional=True
        )) == {
                   'ignore', 'import', 'multi_import', 'override_rule', 'declare', 'maybe', 'literal_range',
                   'literal', 'template_usage', 'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'expansions', 'alias', 'expansion', 'expr', 'atom', 'value',
               }

    def test_list_rules_from_grammar_lark_conditional_inner(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_conditional=True,
            show_inner=True,
        )) == {
                   'ignore', 'import', 'multi_import', 'override_rule', 'declare', 'maybe', 'literal_range',
                   'literal', 'template_usage', 'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'expansions', 'alias', 'expansion', 'expr', 'atom', 'value',
                   'item',
               }

    def test_list_rules_from_grammar_lark_no_alias(self, lark_lark_code):
        assert set(list_rules_from_grammar(grammar_code=lark_lark_code, show_alias=False)) == \
               {
                   'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',
               }

    def test_list_rules_from_grammar_lark_inner_no_alias(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_inner=True,
            show_alias=False
        )) == {
                   'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'item',
               }

    def test_list_rules_from_grammar_lark_conditional_no_alias(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_conditional=True,
            show_alias=False,
        )) == {
                   'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'expansions', 'alias', 'expansion', 'expr', 'atom', 'value',
               }

    def test_list_rules_from_grammar_lark_conditional_inner_no_alias(self, lark_lark_code):
        assert set(list_rules_from_grammar(
            grammar_code=lark_lark_code,
            show_conditional=True,
            show_inner=True,
            show_alias=False,
        )) == {
                   'start', 'rule', 'token', 'rule_params', 'token_params',
                   'priority', 'statement', 'import_path', 'name_list', 'name',

                   'expansions', 'alias', 'expansion', 'expr', 'atom', 'value',
                   'item',
               }
