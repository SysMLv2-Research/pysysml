import pytest
from lark import Lark, UnexpectedCharacters

from pysysml.kerml import __grammar_file__
from pysysml.kerml.models import BoolValue
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


@pytest.mark.unittest
class TestKerMLTransformsLiteral:
    @pytest.mark.parametrize(['text', 'expected'], [
        ('true', True),
        ('false', False),

        # Invalid cases
        ('True', UnexpectedCharacters),  # Case sensitive
        ('False', UnexpectedCharacters),  # Case sensitive
        ('tru', UnexpectedCharacters),  # Typo
        ('fals', UnexpectedCharacters),  # Typo
        ('1', UnexpectedCharacters),  # Not a boolean value
        ('0', UnexpectedCharacters),  # Not a boolean value
        ('yes', UnexpectedCharacters),  # Not a boolean value
        ('no', UnexpectedCharacters),  # Not a boolean value
        ('truth', UnexpectedCharacters),  # Not a boolean value
        ('falsity', UnexpectedCharacters),  # Not a boolean value
    ])
    def test_literal_boolean(self, text, expected):
        parser = _parser_for_rule('literal_boolean')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, BoolValue)
            assert v.raw == text
            assert v.value == expected
            assert rules == ['literal_boolean']
