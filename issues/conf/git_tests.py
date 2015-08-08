import unittest
import tempfile
import subprocess
import shutil
import os

from .git import GitConfig


class GitTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = os.path.join(os.getcwd(), 'test_repo')
        subprocess.check_output([
            'git',
            'init',
            self.repo
        ], cwd=tempfile.tempdir)
        self.git = GitConfig(self.repo)
        self.git['foo.bar'] = 'value'

    def tearDown(self):
        shutil.rmtree(self.repo)

    def test_attribute(self):
        self.assertEqual(self.git.path, self.repo)

    def test_get_repository_path(self):
        self.assertEqual(self.git.repository_path, self.repo)

    def test_get_unknown_value(self):
        with self.assertRaises(KeyError):
            self.git['unknown.option']

    def test_get_unknown_value_with_default(self):
        self.assertIsNone(self.git.get('unknown.option'))

    def test_get_correct_value(self):
        self.assertEqual(self.git['foo.bar'], 'value')

    def test_get_correct_value_with_default(self):
        self.assertEqual(self.git.get('foo.bar'), 'value')
