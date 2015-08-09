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
(id INTEGER PRIMARY KEY, title TEXT)''')
        self.connection.commit()

    def insert_issue(self, id, title):
        with closing(self.connection.cursor()) as cur:
            cur.execute('INSERT INTO issue (id, title) VALUES (?, ?)', (
                id, title))
            self.connection.commit()

    def list_issues(self):
        with closing(self.connection.cursor()) as cur:
            cur.execute('SELECT id, title FROM issue')
            for (id, title) in cur:
                yield (id, title)
