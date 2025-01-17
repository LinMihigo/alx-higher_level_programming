#!/usr/bin/python3
"""
A script that uses GitHub API with Basic Authentication to display the user ID.

Usage:
    ./script.py <username> <personal_access_token>
"""
import requests
import sys


def get_github_id(username, token):
    """
    Uses Basic Authentication to fetch GitHub user ID.

    Args:
        username (str): GitHub username.
        token (str): Personal access token with 'read:user' permission.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Error: Unable to fetch user data")

if __name__ == "__main__":
    get_github_id(sys.argv[1], sys.argv[2])
