# -*- coding: utf-8 -*-

import unittest
import travis

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        pass

    def test_repo_list(self):
        repos = travis.repositories()
        self.assertEqual(type(repos), type(list()))

    def test_repo(self):
        repo = travis.show('travis-ci', 'travis-ci')
        self.assertEqual(type(repo.stable), type(bool()))

    def test_builds_list(self):
        builds = travis.builds('travis-ci', 'travis-ci')
        self.assertEqual(type(builds), type(list()))

    def test_build(self):
        build = travis.show('travis-ci', 'travis-ci')
        self.assertEqual(type(build.last.passed), type(bool()))


if __name__ == '__main__':
    unittest.main()
