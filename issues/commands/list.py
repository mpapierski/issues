import os

import click
from issues.connectors import create_repository


@click.group()
def cli():
    pass


@cli.command()
def list():
    click.echo('listing issues...')
    repo = create_repository(os.environ['GITLAB_URL'], os.environ['GITLAB_TOKEN'])
    for issue in repo.issues():
    	click.echo(issue)
