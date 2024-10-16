import os.path

import pytest


@pytest.mark.unittest
class TestKerMLInit:
    def test_grammar_file(self):
        from pysysml.kerml.cst import __grammar_file__

        assert os.path.exists(__grammar_file__), f'Grammar file not exist, {__grammar_file__!r}'
        assert os.path.isfile(__grammar_file__), f'Grammar file not a file, {__grammar_file__!r}'

        assert os.path.samefile(
            __grammar_file__,
            os.path.normpath(os.path.join('pysysml', 'kerml', 'cst', 'syntax.lark'))
        )
