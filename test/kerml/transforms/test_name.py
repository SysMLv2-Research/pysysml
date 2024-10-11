import pytest
from lark import UnexpectedInput, GrammarError

from pysysml.kerml.models import QualifiedName
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsName:
    @pytest.mark.parametrize(['text', 'expected'], [
        ("myFeature", ("myFeature",)),  # Valid: simple feature reference
        ("pkg::subpackage::feat", ("pkg", "subpackage", "feat")),  # Valid: qualified name
        ("_underscoreFeature", ("_underscoreFeature",)),  # Valid: underscore in name
        ("feature123", ("feature123",)),  # Valid: numbers in name
        ("pkg::feat::subfeature", ("pkg", "feat", "subfeature")),  # Valid: multiple levels
        ("very::long::qualified::feat::name", ("very", "long", "qualified", "feat", "name")),
        # Valid: many levels
        ("double::colon::feat", ("double", "colon", "feat")),  # Valid: double colons
        ("'double with space'::colon::feat", ('double with space', "colon", "feat")),  # Valid: unrestricted colons

        ("123feature", UnexpectedInput),  # Invalid: starts with number
        ("feat-name", UnexpectedInput),  # Invalid: contains hyphen
        ("feat name", UnexpectedInput),  # Invalid: contains space
        ("::leadingColons", UnexpectedInput),  # Invalid: leading colons
        ("trailingColons::", UnexpectedInput),  # Invalid: trailing colons
        ("single:colon", UnexpectedInput),  # Invalid: single colon
        ("package::subpackage::feature", GrammarError),  # Invalid: preserved word
        ("double with space::colon::feat", UnexpectedInput)  # Invalid: invalid spaces
    ])
    def test_qualified_name(self, text, expected):
        parser = _parser_for_rule('qualified_name')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, QualifiedName)
            assert tuple(v.names) == expected
            assert rules == ['qualified_name']
