from __future__ import unicode_literals
import click
from issues.connectors import create_repository
from issues.conf import settings
from issues.database import Database


@click.group()
def cli():
    pass


@cli.command()
def sync():
    '''Push local issues, pull remote issues'''
    click.echo('listing issues...')
    base_url = settings['gitlab.url']
    token = settings['gitlab.token']
    project_name = settings['gitlab.project']
    cache_path = settings['gitlab.cache']
    cache = Database(cache_path)
    # Get local issues to avoid duplicate primary keys
    local_issues = set(id for (id, title) in cache.list_issues())
    repo = create_repository(base_url, token)
    for project in repo.projects:
        if project.name == project_name:
            for issue in repo.issues(project_id=project.id):
                if issue.id not in local_issues:
                    cache.insert_issue(issue.id, issue.title)
                    click.echo('New issue cached {0}'.format(issue.title))
            break
