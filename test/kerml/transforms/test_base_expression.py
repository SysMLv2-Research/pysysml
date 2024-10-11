import pytest
from lark import UnexpectedInput

from pysysml.kerml.models import NullValue
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
