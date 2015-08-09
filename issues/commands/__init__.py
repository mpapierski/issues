import click
from .list import cli as list_cli
from .sync import cli as sync_cli
from .new import cli as new_cli

collection = click.CommandCollection(sources=[
    list_cli,
    sync_cli,
    new_cli])
