"""

Test case for the github get repository name and number of commits.

"""

import unittest
from github_api import github_user_info


class TestGitHubAPI(unittest.TestCase):

    def test_githubapi(self):

        repository = [value for value in github_user_info("richkempinski")]
        result = ['Repo: csp, Number of commits: 2',
                  'Repo: hellogitworld, Number of commits: 30',
                  'Repo: helloworld, Number of commits: 6',
                  'Repo: Mocks, Number of commits: 10',
                  'Repo: Project1, Number of commits: 2',
                  'Repo: richkempinski.github.io, Number of commits: 9',
                  'Repo: threads-of-life, Number of commits: 1',
                  'Repo: try_nbdev, Number of commits: 2',
                  'Repo: try_nbdev2, Number of commits: 5']
        self.assertEqual(repository, result)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
