from __future__ import unicode_literals
from StringIO import StringIO

import click

from issues.conf import settings
from issues.database import Database


@click.group()
def cli():
    pass


@cli.command()
def list():
    '''List all cached issues'''
    db = Database(settings['gitlab.cache'])
    content = StringIO()
    for (id, title, description) in db.issues:
        if id is None:
            content.write('Issue: {0}\n'.format(title))
        else:
            content.write('Issue: {0} (#{1})\n'.format(title, id))
        content.write(description + '\n')
        content.write('---\n')
    click.echo_via_pager(content.getvalue())
