import click

from .base import CONTEXT_SETTINGS
from ..kerml import resource_file_check


def _add_health_subcommand(cli: click.Group) -> click.Group:
    @cli.command('health', help='Do health check.',
                 context_settings=CONTEXT_SETTINGS)
    def clone():
        resource_file_check()
        click.echo('Everything is okay!')

    return cli
