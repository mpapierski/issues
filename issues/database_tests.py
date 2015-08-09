import unittest

from .database import Database


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        self.db = Database(':memory:')

    def tearDown(self):
        pass

    def test_empty_issues(self):
        with self.assertRaises(StopIteration):
            next(self.db.issues)

    def test_no_pending_issues(self):
        with self.assertRaises(StopIteration):
            next(self.db.pending_issues)

    def test_insert_issue(self):
        self.db.insert_issue(123, 'Title')
        (id, title, ) = next(self.db.issues)
        self.assertEqual(id, 123)
        self.assertEqual(title, 'Title')

        with self.assertRaises(StopIteration):
            next(self.db.pending_issues)

    def test_insert_pending_issue(self):
        self.db.insert_issue(None, 'Title')
        (id, title, ) = next(self.db.issues)
        self.assertIsNone(id)
        self.assertEqual(title, 'Title')

        (id, title, ) = next(self.db.pending_issues)
        self.assertIsNone(id)
        self.assertEqual(title, 'Title')
