import os

import pytest
from hbutils.random import random_sha1_with_timestamp
from lark import Lark, GrammarError, UnexpectedCharacters, Token, UnexpectedEOF

from pysysml.kerml.models import Name
from pysysml.kerml.transform import tree_to_cst


def _parser_for_token(token_name):
    start_name = f'start_{random_sha1_with_timestamp()}'
    grammar_code = f"""
%import .pysysml.kerml.syntax.{token_name}

{start_name}: {token_name}

%import common.WS
%ignore WS
    """
    lark = Lark(
        grammar_code,
        start=[start_name],
        import_paths=[os.getcwd()]
    )

    def _parse(x):
        node = tree_to_cst(lark.parse(x, start=start_name))
        return node.children[0]

    return _parse


@pytest.mark.unittest
class TestKerMLTransform:
    @pytest.mark.parametrize(['text', 'expected'], [
        # normal cases
        ('abc', 'abc'),
        ('variable', 'variable'),
        ('functionName', 'functionName'),
        ('class_name', 'class_name'),
        ('_private_var', '_private_var'),
        ('CONSTANT_VALUE', 'CONSTANT_VALUE'),
        ('camelCase', 'camelCase'),
        ('snake_case', 'snake_case'),
        ('mixedCase_123', 'mixedCase_123'),
        ('with_number1', 'with_number1'),
        ('_123numericStart', '_123numericStart'),

        # invalid cases
        ('123startWithDigit', UnexpectedCharacters),  # starts with a digit
        ('has space', UnexpectedCharacters),  # contains a space
        ('special#char', UnexpectedCharacters),  # contains a special character #
        ('hello-world', UnexpectedCharacters),  # contains a hyphen
        ('contains!mark', UnexpectedCharacters),  # contains an exclamation mark
        ('use$sign', UnexpectedCharacters),  # contains a dollar sign
        ('percent%25', UnexpectedCharacters),  # contains a percent sign
        ('weird&char', UnexpectedCharacters),  # contains an ampersand
        ('*star', UnexpectedCharacters),  # starts with an asterisk
        ('(parens)', UnexpectedCharacters),  # contains parentheses
        ('plus+plus', UnexpectedCharacters),  # contains a plus sign
        ('semicolon;', UnexpectedCharacters),  # contains a semicolon
        ('colon:colon', UnexpectedCharacters),  # contains a colon
        ('comma,comma', UnexpectedCharacters),  # contains a comma
        ('quote"quote', UnexpectedCharacters),  # contains a double quote
        ('single\'quote', UnexpectedCharacters),  # contains a single quote
        ('backslash\\test', UnexpectedCharacters),  # contains a backslash
        ('brace{test}', UnexpectedCharacters),  # contains a brace
        ('bracket[test]', UnexpectedCharacters),  # contains a bracket
        ('pipe|pipe', UnexpectedCharacters),  # contains a pipe
        ('tilde~tilde', UnexpectedCharacters),  # contains a tilde
        ('question?mark', UnexpectedCharacters),  # contains a question mark
        ("ksdjfl  233", UnexpectedCharacters),

        # unrestricted words
        ("'ksdjfl'", "'ksdjfl'"),
        ("'ksdjfl  233'", "'ksdjfl  233'"),
        ("'   ksdjfl\\t  233'", "'   ksdjfl\\t  233'"),
        ("'hello\\nworld'", "'hello\\nworld'"),
        ("'escape\\rsequence'", "'escape\\rsequence'"),
        ("'backspace\\bchar'", "'backspace\\bchar'"),
        ("'form\\ffeed'", "'form\\ffeed'"),
        ("'single\\'quote'", "'single\\'quote'"),
        ("'double\\\"quote'", "'double\\\"quote'"),
        ("'中文字符'", "'中文字符'"),
        ("'日本語'", "'日本語'"),
        ("'한글'", "'한글'"),
        ("'русский'", "'русский'"),
        ("'\\t\\n\\r\\b\\f'", "'\\t\\n\\r\\b\\f'"),
        ("'multiple\\t\\t\\tescapes'", "'multiple\\t\\t\\tescapes'"),
        ("'mixed 中文 with English'", "'mixed 中文 with English'"),
        ("'special_chars_!@#$%^&*()'", "'special_chars_!@#$%^&*()'"),
        ("'1234567890'", "'1234567890'"),
        ("'" + "long string " * 20 + "'", "'" + "long string " * 20 + "'"),
        ("'\\'escaping edge case'", "'\\'escaping edge case'"),
        ("'\\''", "'\\''"),
        ("''", "''"),
        ("' '", "' '"),

        # invalid unrestricted words
        ('"ksdjfl"', UnexpectedCharacters),  # Invalid because it starts with a double quote instead of a single quote
        ("'   ksdjfl\\a  233'", UnexpectedCharacters),  # Invalid because '\\a' is not a supported escape character
        ("'   ksdjfl  233\\'", UnexpectedCharacters),  # Invalid because it ends with a lone backslash
        ("'unterminated", UnexpectedCharacters),
        # Invalid because it starts with a single quote but does not end with one
        ("ksdjfl'", UnexpectedCharacters),  # Invalid because it ends with a single quote but does not start with one
        ("'ksdjfl", UnexpectedCharacters),  # Invalid because it starts with a single quote but does not end with one
        ("'\\x20'", UnexpectedCharacters),  # Invalid because '\\x' hex escape is not supported
        ("'\\u1234'", UnexpectedCharacters),  # Invalid because '\\u' unicode escape is not supported
        ("'\\U0001F600'", UnexpectedCharacters),  # Invalid because '\\U' unicode escape is not supported
        ("'\\123'", UnexpectedCharacters),  # Invalid because octal escapes are not supported
        ("'\\777'", UnexpectedCharacters),  # Invalid because octal escapes are not supported
        ("'invalid\\escape'", UnexpectedCharacters),  # Invalid because '\\escape' is not a recognized escape sequence
        ("'another\\invalid\\escape'", UnexpectedCharacters),
        # Invalid because '\\invalid' is not a recognized escape sequence
        ("'wrong\\escape\\sequence'", UnexpectedCharacters),
        # Invalid because '\\escape' and '\\sequence' are not recognized escape sequences
        ("'\\'", UnexpectedCharacters),  # Invalid because it contains a lone backslash which is not escaping anything
        ("'\\n\\r\\b\\t\\f\\'\\\"'", "'\\n\\r\\b\\t\\f\\'\\\"'"),
        # Correctly escaped characters including single and double quotes
        ("'\\n\\r\\b\\t\\f\\'\\\"'*10", UnexpectedCharacters),  # Invalid because it ends with an unescaped single quote

        # preserved words
        ('about', GrammarError),
        ('abstract', GrammarError),
        ('alias', GrammarError),
        ('all', GrammarError),
        ('and', GrammarError),
        ('as', GrammarError),
        ('assoc', GrammarError),
        ('behavior', GrammarError),
        ('binding', GrammarError),
        ('bool', GrammarError),
        ('by', GrammarError),

    ])
    def test_name(self, text: str, expected):
        token_name_parser = _parser_for_token('NAME')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = token_name_parser(text)
        else:
            assert token_name_parser(text) == Name(text)

    @pytest.mark.parametrize(['text', 'expected'], [
        # Valid single line comments
        ('// This is a comment', '// This is a comment'),
        ('//Another comment', '//Another comment'),
        ('//12345', '//12345'),

        # Invalid single line comments
        ('/ This is not a comment', UnexpectedCharacters),  # missing second slash
        ('// This is not a multiline /* comment */', '// This is not a multiline /* comment */'),  # valid single line
        ('//', '//'),  # valid single line, empty comment

    ])
    def test_single_line_note(self, text: str, expected):
        single_line_note_parser = _parser_for_token('SINGLE_LINE_NOTE')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = single_line_note_parser(text)
        else:
            assert single_line_note_parser(text) == Token('SINGLE_LINE_NOTE', text)

    @pytest.mark.parametrize(['text', 'expected'], [
        # Valid multiline notes
        ('//* This is a multiline comment */', '//* This is a multiline comment */'),
        ('//* Multiline\ncomment */', '//* Multiline\ncomment */'),
        ('//*12345*/', '//*12345*/'),

        # Invalid multiline notes
        ('/* This is not a multiline note */', UnexpectedCharacters),  # wrong start sequence
        ('//* This is not closed', UnexpectedCharacters),  # not properly closed
        ('//* */', '//* */'),  # valid, empty multiline note
    ])
    def test_multiline_note(self, text: str, expected):
        multiline_note_parser = _parser_for_token('MULTILINE_NOTE')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = multiline_note_parser(text)
        else:
            assert multiline_note_parser(text) == Token('MULTILINE_NOTE', text)

    @pytest.mark.parametrize(['text', 'expected'], [
        # Valid regular comments
        ('/* This is a comment */', '/* This is a comment */'),
        ('/* Multiline\ncomment */', '/* Multiline\ncomment */'),
        ('/*12345*/', '/*12345*/'),

        # Invalid regular comments
        ('//* This is not a regular comment */', UnexpectedCharacters),  # wrong start sequence
        ('/* This is not closed', UnexpectedCharacters),  # not properly closed
        ('/* */', '/* */'),  # valid, empty regular comment
    ])
    def test_regular_comment(self, text: str, expected):
        regular_comment_parser = _parser_for_token('REGULAR_COMMENT')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = regular_comment_parser(text)
        else:
            assert regular_comment_parser(text) == Token('REGULAR_COMMENT', text)

    @pytest.mark.parametrize(['text', 'expected'], [
        # Valid DECIMAL_VALUE cases
        ('0', '0'),  # single digit
        ('123', '123'),  # multiple digits
        ('456789', '456789'),  # larger number

        # Invalid DECIMAL_VALUE cases
        ('', UnexpectedEOF),  # empty string
        ('abc', UnexpectedCharacters),  # non-digit characters
        ('12.34', UnexpectedCharacters),  # contains a decimal point
        ('-123', UnexpectedCharacters),  # negative sign not allowed
        ('123abc', UnexpectedCharacters),  # trailing non-digit characters
    ])
    def test_decimal_value(self, text: str, expected):
        decimal_value_parser = _parser_for_token('DECIMAL_VALUE')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = decimal_value_parser(text)
        else:
            assert decimal_value_parser(text) == text

    @pytest.mark.parametrize(['text', 'expected'], [
        # Valid EXPONENTIAL_VALUE cases
        ('1e10', '1e10'),  # simple exponential
        ('2E+5', '2E+5'),  # positive exponent with plus sign
        ('3E-2', '3E-2'),  # negative exponent
        ('123e45', '123e45'),  # larger base and exponent

        # Invalid EXPONENTIAL_VALUE cases
        ('e10', UnexpectedCharacters),  # missing base
        ('10E', UnexpectedCharacters),  # missing exponent
        ('10e+', UnexpectedCharacters),  # missing exponent number
        ('10e-5.5', UnexpectedCharacters),  # fractional exponent not allowed
        ('abcE10', UnexpectedCharacters),  # non-digit base
        ('10eabc', UnexpectedCharacters),  # non-digit exponent
        ('10e 5', UnexpectedCharacters),  # space between exponent
    ])
    def test_exponential_value(self, text: str, expected):
        exponential_value_parser = _parser_for_token('EXPONENTIAL_VALUE')
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = exponential_value_parser(text)
        else:
            assert exponential_value_parser(text) == text
