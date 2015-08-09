from __future__ import unicode_literals
import sys

import click
# from issues.connectors import create_repository
# from issues.conf import settings
from issues.utils import call_editor


def is_comment(text):
    return text.startswith('#')


@click.group()
def cli():
    pass


@cli.command()
def new():
    # base_url = settings['gitlab.url']
    # token = settings['gitlab.token']
    # project_name = settings['gitlab.project']
    # repo = create_repository(base_url, token)
    template = '''# Commented lines are ignored
#
# Example:
#
# This is title of issue
#
# This is longer description
#
'''
    result = call_editor(template)
    if result is not None:
        lines = [line for line in result.splitlines() if not is_comment(line)]
        if not lines:
            result = None

    if result is None:
        sys.stderr.write('Empty message found...\n')
        sys.exit(1)

    for line in lines:
        click.echo('{0!r}'.format(line))
