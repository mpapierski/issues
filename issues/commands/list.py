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
    repo = create_repository(base_url, token)
    for issue in repo.issues():
        click.echo(issue)
