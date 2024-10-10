import os

import pytest
from hbutils.random import random_sha1_with_timestamp
from lark import Lark, GrammarError, UnexpectedCharacters

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


@pytest.fixture()
def token_name_parser():
    return _parser_for_token('NAME')


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
        ('"ksdjfl"', UnexpectedCharacters),
        ("'   ksdjfl\\a  233'", UnexpectedCharacters),
        ("'   ksdjfl  233\\'", UnexpectedCharacters),
        ("'unterminated", UnexpectedCharacters),
        ("ksdjfl'", UnexpectedCharacters),
        ("'ksdjfl", UnexpectedCharacters),
        ("'\\x20'", UnexpectedCharacters),
        ("'\\u1234'", UnexpectedCharacters),
        ("'\\U0001F600'", UnexpectedCharacters),
        ("'\\123'", UnexpectedCharacters),
        ("'\\777'", UnexpectedCharacters),
        ("'invalid\\escape'", UnexpectedCharacters),
        ("'another\\invalid\\escape'", UnexpectedCharacters),
        ("'wrong\\escape\\sequence'", UnexpectedCharacters),
        ("'\\'", UnexpectedCharacters),
        ("'\\n\\r\\b\\t\\f\\'\\\"'", "'\\n\\r\\b\\t\\f\\'\\\"'"),
        ("'\\n\\r\\b\\t\\f\\'\\\"'*10", UnexpectedCharacters),

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
    def test_name(self, token_name_parser, text: str, expected):
        # \(('[a-zA-Z\d_]+'), True\),
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                _ = token_name_parser(text)
        else:
            assert token_name_parser(text) == Name(text)
