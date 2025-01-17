#!/usr/bin/python3
"""
A script that sends a request to a URL and displays the value of the
X-Request-Id variable in the response header.

Usage:
    ./script.py <URL>
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Sends a request to the given URL and displays the X-Request-Id value.

    Args:
        url (str): The URL to request.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)

if __name__ == "__main__":
    fetch_x_request_id(sys.argv[1])
