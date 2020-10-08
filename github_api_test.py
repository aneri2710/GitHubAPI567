"""

Test case for the github get repository name and number of commits.

"""
import os
import unittest
from mock import patch
from github_api import github_user_info
import json


class TestGitHubAPI(unittest.TestCase):

    def test_wrong_user_id(self):

        mock_patcher = patch('requests.get')
        mock_get = mock_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/file_not_found.json') as f:
            mock_get.return_value = json.load(f)
        mock_patcher.stop()
        get_fun = mock_get()
        self.assertEqual(get_fun.get('message'), "Not Found")

    def test_githubapi(self):
        mock_patcher = patch('requests.get')
        mock_get = mock_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/rich.json') as f:
            mock_get.return_value = json.load(f)
        mock_patcher.stop()
        get_fun = mock_get()
        self.assertEqual(len(get_fun), 73)



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
