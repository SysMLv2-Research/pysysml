from .dispatch import pysysmlcli
from .health import _add_health_subcommand

# add adding methods here
_DECORATORS = [
    _add_health_subcommand,
]

cli = pysysmlcli
for deco in _DECORATORS:
    cli = deco(cli)
