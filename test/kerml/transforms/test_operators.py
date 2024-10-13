import pytest

from pysysml.kerml.models import ExtentOp, QualifiedName, IntValue, RealValue, UnaryOp, StringValue, InfValue
from .base import _parser_for_rule


@pytest.mark.unittest
class TestKerMLTransformsOperator:
    @pytest.mark.parametrize(['text', 'expected'], [
        ('all x', ExtentOp(x=QualifiedName(names=['x']))),
        ('+2', UnaryOp(op='+', x=IntValue(raw='2'))),
        ('-1.4', UnaryOp(op='-', x=RealValue(raw='1.4'))),
        ('~ x::y', UnaryOp(op='~', x=QualifiedName(names=['x', 'y']))),
        ("not x::'+'", UnaryOp(op='not', x=QualifiedName(names=['x', '+']))),
        ('~ "x y z +"', UnaryOp(op='~', x=StringValue(raw='"x y z +"'))),
        ('1', IntValue(raw='1')),
        ('1.5', RealValue(raw='1.5')),
        ('.5e-2', RealValue(raw='.5e-2')),
        ('"123 456"', StringValue(raw='"123 456"')),
        ('*', InfValue()),
        ('-*', UnaryOp(op='-', x=InfValue())),
    ])
    @pytest.mark.focus
    def test_owned_expression(self, text, expected):
        parser = _parser_for_rule('owned_expression')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert v == expected
            # assert 'owned_expression' in rules
