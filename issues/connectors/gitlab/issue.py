from .user import User


class Issue(object):

    '''GitLab issue

    Represents project's issue.
    '''
    url = '/issues'

    def __init__(self, description, title, created_at, labels, updated_at, iid,
                 state, assignee, author, milestone, project_id, id):
        self.description = description
        self.title = title
        self.created_at = created_at
        self.labels = labels
        self.updated_at = updated_at
        self.iid = iid
        self.state = state
        self.assignee = User(**assignee)
        self.author = User(**author)
        self.milestone = milestone
        self.project_id = project_id
        self.id = id

    def __repr__(self):
        return 'Issue({0})'.format(self.title)
