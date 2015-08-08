import requests
from .issue import Issue


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

    def issues(self):
        issues = requests.get(self.url + Issue.url, headers=self.headers)
        return [Issue(**issue) for issue in issues.json()]
