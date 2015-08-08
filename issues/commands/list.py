from __future__ import unicode_literals
import click
from issues.connectors import create_repository
from issues.conf import settings


@click.group()
def cli():
    pass


@cli.command()
def list():
    click.echo('listing issues...')
    base_url = settings['gitlab.url']
    token = settings['gitlab.token']
    project_name = settings['gitlab.project']
    repo = create_repository(base_url, token)
    for project in repo.projects:
        if project.name == project_name:
            for issue in repo.issues(project_id=project.id):
                click.echo(issue)
