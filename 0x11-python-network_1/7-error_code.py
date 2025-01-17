#!/usr/bin/python3
"""
A script that sends a request to a URL and displays the body of the response.
Handles HTTP status codes greater than or equal to 400.

Usage:
    ./script.py <URL>
"""
import requests
import sys


def fetch_url_body(url):
    """
    Sends a request to the given URL and displays the response body.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url_body(sys.argv[1])
