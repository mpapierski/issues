import click
from .list import cli as list_cli
from .sync import cli as sync_cli

collection = click.CommandCollection(sources=[
    list_cli,
    sync_cli])
