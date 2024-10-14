import math

import pytest
from lark import UnexpectedCharacters

from pysysml.kerml.models import BoolValue, IntValue, RealValue, StringValue, InfValue
from .base import _parser_for_rule


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

    @pytest.mark.parametrize(['text', 'expected'], [
        ("42", 42),  # Valid: positive integer
        ("0", 0),  # Valid: zero
        ("007", 7),  # Valid: leading zeros

        ("-42", UnexpectedCharacters),  # Invalid: negative sign not part of integer literal
        ("3.14", UnexpectedCharacters),  # Invalid: decimal point not allowed in integer
    ])
    def test_literal_integer(self, text, expected):
        parser = _parser_for_rule('literal_integer')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, IntValue)
            assert v.raw == text
            assert v.value == expected
            assert rules == ['literal_integer']

    @pytest.mark.parametrize(['text', 'expected'], [
        ("3.14", 3.14),  # Valid: simple real number
        (".5", 0.5),  # Valid: leading decimal point
        ("1e10", 1e10),  # Valid: exponential notation
        ("6.022E23", 6.022e23),  # Valid: exponential notation with capital E
        ("1.6e-19", 1.6e-19),  # Valid: negative exponent

        ("1e", UnexpectedCharacters),  # Invalid: incomplete exponential notation
        ("1.2.3", UnexpectedCharacters),  # Invalid: multiple decimal points
        ("2.", UnexpectedCharacters),  # Invalid: point must have suffix
    ])
    def test_literal_real(self, text, expected):
        parser = _parser_for_rule('literal_real')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, RealValue)
            assert v.raw == text
            assert v.value == pytest.approx(expected)
            assert rules == ['literal_real']

    @pytest.mark.parametrize(['text', 'expected'], [
        ('"Hello, World!"', "Hello, World!"),  # Valid: simple string
        ('"Escape \\"quotes\\""', "Escape \"quotes\""),  # Valid: escaped quotes
        ('"Line\\nbreak"', "Line\nbreak"),  # Valid: escaped newline

        ('"Incomplete string', UnexpectedCharacters),  # Invalid: unclosed string
        ('"Invalid \escape"', UnexpectedCharacters),  # Invalid: incorrect escape sequence
    ])
    def test_literal_string(self, text, expected):
        parser = _parser_for_rule('literal_string')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, StringValue)
            assert v.raw == text
            assert v.value == expected
            assert rules == ['literal_string']

    @pytest.mark.parametrize(['text', 'expected'], [
        ("*", math.inf),  # Valid: infinity symbol
        ("**", UnexpectedCharacters),  # Invalid: multiple asterisks
    ])
    def test_literal_infinity(self, text, expected):
        parser = _parser_for_rule('literal_infinity')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = parser(text)
        else:
            v, rules = parser(text)
            assert isinstance(v, InfValue)
            assert v.value == pytest.approx(expected)
            assert rules == ['literal_infinity']
