import sys
import textwrap
from pprint import pformat
from typing import List


def print_cases(start: str, cases: List[str], file=sys.stdout):
    from test.kerml.transforms.base import _parser_for_rule

    parser = _parser_for_rule(start)
    print(f"@pytest.mark.parametrize(['text', 'expected'], [", file=file)
    for case in cases:
        case = textwrap.dedent(case).strip()
        v = (case, parser(case)[0])
        print('    ' + pformat(v) + ',', file=file)
    print(f"])", file=file)
    print(f"@pytest.mark.focus", file=file)
    print(f"def test_{start}(self, text, expected):", file=file)
    print(f"    parser = _parser_for_rule({start!r})", file=file)
    print(f"    if isinstance(expected, type) and issubclass(expected, Exception):", file=file)
    print(f"        with pytest.raises(expected):", file=file)
    print(f"            _ = parser(text)", file=file)
    print(f"    else:", file=file)
    print(f"        v, rules = parser(text)", file=file)
    print(f"        assert v == expected", file=file)
    print(f"        assert {start!r} in rules", file=file)
