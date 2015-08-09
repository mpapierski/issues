from __future__ import unicode_literals
import sys

import click
# from issues.connectors import create_repository
from issues.conf import settings
from issues.database import Database


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
    cache_path = settings['gitlab.cache']
    cache = Database(cache_path)

    template = '''# Commented lines are ignored
#
# Example:
#
# This is title of issue
#
# This is longer description
#
'''
    result = click.edit(template)
    if result is not None:
        lines = [line for line in result.splitlines() if not is_comment(line)]
        if not lines:
            result = None

    if result is None:
        sys.stderr.write('Empty message found...\n')
        sys.exit(1)

    title = lines[0]
    description = ''

    if len(lines) >= 2:
        # Title
        # empty line
        # Long description
        description = '\n'.join(lines[2:])

    cache.insert_issue(None, title, description)
    click.echo('New issue added.')
    click.echo('Please `sync` now to push local issues to your remote')
