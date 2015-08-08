from .user import User


class Issue(object):

    '''GitLab issue

    Represents project's issue.
    '''

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

    @classmethod
    def get_url(cls, project_id=None, state=None, labels=None):
        if project_id is not None:
            url = '/projects/{0}/issues'.format(project_id)
        else:
            url = '/issues'
        qs = []
        if state is not None:
            qs.append('state={0}'.format(state))
        if labels is not None:
            comma_labels = ','.join(labels)
            qs.append('labels={0}'.format(comma_labels))
        return url + '?' + '&'.join(qs)

    def __repr__(self):
        return 'Issue({0})'.format(self.title)
