#!/usr/bin/python3
"""
A script that sends a request to a URL and displays the body of the response,
decoded in UTF-8. Handles HTTPError exceptions.

Usage:
    ./script.py <URL>
"""
import urllib.request
import urllib.error
import sys


def fetch_url_body(url):
    """
    Sends a request to the given URL and displays the response body.

    Args:
        url (str): The URL to request.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    fetch_url_body(sys.argv[1])
