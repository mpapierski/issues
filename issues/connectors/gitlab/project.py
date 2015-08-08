from __future__ import unicode_literals
from .user import User
from .namespace import Namespace


class Project(object):

    '''Representation of a project
    '''
    url = '/projects/all'

    def __init__(self, id, description, default_branch, public,
                 visibility_level, ssh_url_to_repo, http_url_to_repo, web_url,
                 name, name_with_namespace, path, path_with_namespace,
                 issues_enabled, merge_requests_enabled, wiki_enabled,
                 snippets_enabled, created_at, last_activity_at, namespace,
                 archived, owner=None):
        self.id = id
        self.description = description
        self.default_branch = default_branch
        self.public = public
        self.visibility_level = visibility_level
        self.ssh_url_to_repo = ssh_url_to_repo
        self.http_url_to_repo = http_url_to_repo
        self.web_url = web_url
        self.name = name
        self.name_with_namespace = name_with_namespace
        self.path = path
        self.path_with_namespace = path_with_namespace
        self.issues_enabled = issues_enabled
        self.merge_requests_enabled = merge_requests_enabled
        self.wiki_enabled = wiki_enabled
        self.snippets_enabled = snippets_enabled
        self.created_at = created_at
        self.last_activity_at = last_activity_at
        self.namespace = Namespace(**namespace)
        self.archived = archived
        self.owner = User(**owner) if owner else None

    def get_url(self):
        return ('/projects', {})

    def __repr__(self):
        return 'Project({0})'.format(self.name)
