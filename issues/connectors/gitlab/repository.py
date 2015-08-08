import itertools
import requests
from .issue import Issue
from .project import Project


class Repository(object):

    '''Represents a GitLab connection to a repository
    '''

    def __init__(self, url, token=None):
        self.url = '{0}/api/v3'.format(url)
        self.token = token
        self.headers = {
            'PRIVATE-TOKEN': token
        }

    def auth(self):
        '''Perform authentication.

        Uses private token.
        '''

    def _api_get_list(self, url):
        '''Returns list of objects assuming pagination
        '''
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        for item in r.json():
            yield item
        next_url = r.links.get('next')
        if next_url is not None:
            for item in self._api_get_list(next_url['url']):
                yield item

    @property
    def projects(self):
        '''Lists all projects
        '''
        projects = self._api_get_list(self.url + Project.url)
        return [Project(**project) for project in projects]

    def issues(self, project_id=None, state=None, labels=None):
        '''List issues with filter.
        '''
        url = self.url + Issue.get_url(
            project_id=project_id,
            state=state,
            labels=labels)
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        data = r.json()
        return [Issue(**issue) for issue in data]
