import subprocess


class GitConfig(object):

    '''Wrapper to read config values from git repo.

    Pass `path` which might be possibly inside git repo.
    '''

    def __init__(self, path):
        self.path = path

    @property
    def repository_path(self):
        '''Discovers top level path inside repo
        '''
        git_root = subprocess.check_output([
            'git',
            'rev-parse',
            '--show-toplevel'], cwd=self.path)
        return git_root.splitlines()[0]

    def __git(self, *args):
        '''Calls git executable with arguments

        This will allways call git inside the repo regardless of the actual
        location of git repo.
        '''
        return subprocess.check_output(('git', ) + args,
                                       cwd=self.repository_path)

    def __getitem__(self, key):
        '''Gets value from git repository.

        Raises KeyError when key does not exists.
        '''
        try:
            stdout = self.__git(
                'config',
                '-z',  # "zero" - his makes the value machine readable
                '--get',
                key)
            (value, _) = stdout.split('\x00', 1)
            return value
        except subprocess.CalledProcessError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        '''Sets value in git config

        Uses git-config(1) internally.
        '''
        self.__git('config', key, value)

    def get(self, key, default_value=None):
        '''Gets value from config.

        When the config value does not exists, returns default_value.
        '''
        try:
            return self[key]
        except KeyError:
            return default_value
