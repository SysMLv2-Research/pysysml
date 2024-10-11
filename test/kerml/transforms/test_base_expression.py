import pytest
from lark import UnexpectedInput, GrammarError

from pysysml.kerml.models import NullValue, MetadataAccessExpression, QualifiedName
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsBaseExpression:
    @pytest.mark.parametrize(['text', 'expected'], [
        ("null", None),  # Valid: null expression
        ("()", None),  # Valid: empty parentheses as null
        ("(  )", None),  # Valid: empty parentheses with whitespace
        ("( )", None),  # Valid: parentheses with space
        ("Null", UnexpectedInput),  # Invalid: case sensitive
        ("NULL", UnexpectedInput),  # Invalid: all caps
        ("(null)", UnexpectedInput),  # Invalid: null in parentheses
        ("(,)", UnexpectedInput),  # Invalid: comma in empty parentheses
        ("(())", UnexpectedInput),  # Invalid: nested empty parentheses
    ])
    def test_null_expression(self, text, expected):
        parser = _parser_for_rule('null_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, NullValue)
            assert v.value is None
            assert rules == ['null_expression']

    @pytest.mark.parametrize(['text', 'expected'], [
        ("pkg.metadata", ('pkg',)),  # Valid: simple metadata access
        ("very::long::qualified::name.metadata", ('very', 'long', 'qualified', 'name')),  # Valid: long qualified name
        ("'very long'::qualified::name.metadata", ('very long', 'qualified', 'name')),  # Valid: long qualified name
        ("_package.metadata", ('_package',)),  # Valid: underscore in package name
        ("package123.metadata", ('package123',)),  # Valid: numbers in package name
        ("PACKAGE.metadata", ('PACKAGE',)),  # Valid: uppercase package name
        ("pkg::subpackage.metadata", ('pkg', 'subpackage')),  # Valid: qualified name with double colons

        ("package.metadata", GrammarError),  # Valid: reserved word
        ("package.Metadata", UnexpectedInput),  # Invalid: uppercase 'Metadata'
        ("package.meta_data", UnexpectedInput),  # Invalid: underscore in 'metadata'
        (".metadata", UnexpectedInput),  # Invalid: leading dot
        ("package.", UnexpectedInput),  # Invalid: trailing dot
        ("package..metadata", UnexpectedInput),  # Invalid: double dot
        ("package.metadata.extra", UnexpectedInput),  # Invalid: extra after 'metadata'
        ("package.metaData", UnexpectedInput),  # Invalid: camelCase 'metadata'
    ])
    def test_metadata_access_expression(self, text, expected):
        parser = _parser_for_rule('metadata_access_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, MetadataAccessExpression)
            assert v.qualified_name == QualifiedName(list(expected))
            assert set(rules) == {'qualified_name', 'metadata_access_expression'}

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
    def test_feature_reference_expression(self, text, expected):
        parser = _parser_for_rule('feature_reference_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, QualifiedName)
            assert tuple(v.names) == expected
            assert set(rules) == {'qualified_name'}
