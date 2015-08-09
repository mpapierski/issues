import sqlite3
from contextlib import closing


class Database(object):
    '''Database implementation

    Provides methods to easily access tables.
    '''
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self._create_tables()

    def __del__(self):
        self.connection.close()

    def _create_tables(self):
        '''Creates database structure
        '''
        c = self.connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS issue
(id INTEGER UNIQUE, title TEXT)''')
        self.connection.commit()

    def insert_issue(self, id, title):
        '''Inserts new issue into database'''
        with closing(self.connection.cursor()) as cur:
            cur.execute('INSERT INTO issue (id, title) VALUES (?, ?)', (
                id, title))
            self.connection.commit()

    @property
    def issues(self):
        '''Lists all issues'''
        with closing(self.connection.cursor()) as cur:
            cur.execute('SELECT id, title FROM issue')
            for row in cur:
                yield row

    @property
    def pending_issues(self):
        '''List of all pending issues

        A pending issue is an issue without id property assigned
        '''
        with closing(self.connection.cursor()) as cur:
            cur.execute('SELECT id, title FROM issue WHERE id IS NULL')
            for row in cur:
                yield row
