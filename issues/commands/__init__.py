import click
from .list import cli

collection = click.CommandCollection(sources=[cli])
