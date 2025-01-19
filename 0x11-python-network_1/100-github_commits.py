#!/usr/bin/python3
"""contains get_commits"""
import requests
import sys


def get_commits(repo, owner):
    """
    Retrieves the 10 most recent commits from a GitHub repository.

    Args:
        repo (str): The name of the repository.
        owner (str): The owner of the repository.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    result = []
    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit", {}).get("author", {}).get("name")
        result.append(f"{sha}: {author}")
    return result


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    commits = get_commits(repo, owner)

    for commit in commits:
        print(commit)
