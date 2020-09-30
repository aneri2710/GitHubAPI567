"""
Author : Aneri Shah
CWID : 10451737

Homework 4- To get the repository name, number of commits from the user ID from github.

"""
import requests
import json


def github_user_info(userID):
    # check if the user id is invalid
    if userID is None:
        return "Input is invalid"
    # check if the user is is not a string
    if not isinstance(userID, str):
        raise ValueError(f"{userID} is not a string.")

    user_repo = "https://api.github.com/users/" + userID + "/repos"

    get_repos = requests.get(user_repo)
    repos_json = get_repos.json()

    for value in repos_json:
        repository_name = value["name"]
        commits = "https://api.github.com/repos/" + userID + "/" + repository_name + "/commits"
        get_commits = requests.get(commits)
        commits_json = get_commits.json()
        count = 0
        # check if the number of commits are 0
        if commits_json == 0:
            print("no commits")

        for c in commits_json:
            count += 1
        yield f"Repo: {repository_name}, Number of commits: {count}"


def main():
    # get the user id
    userID = input("Enter your user ID: ")
    for i in github_user_info(userID):
        return i
