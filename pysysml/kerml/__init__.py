import os.path

from .base import list_reserved_words, is_reserved_word

__grammar_file__ = os.path.normpath(os.path.join(__file__, '..', 'syntax.lark'))
