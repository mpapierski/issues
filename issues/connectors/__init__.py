from .gitlab.repository import Repository


def create_repository(url, token):
    '''Creates repository connection
    '''
    # TODO: Make some guessing about server type
    return Repository(url, token)
