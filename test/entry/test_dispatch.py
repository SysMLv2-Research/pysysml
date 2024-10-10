import pytest
from hbutils.testing import simulate_entry

from pysysml.config.meta import __VERSION__
from pysysml.entry import pysysmlcli


@pytest.mark.unittest
class TestEntryDispatch:
    def test_version(self):
        result = simulate_entry(pysysmlcli, ['pysysml', '-v'])
        assert result.exitcode == 0
        assert __VERSION__ in result.stdout
