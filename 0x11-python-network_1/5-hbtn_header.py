#!/usr/bin/python3
"""
A script that sends a request to a URL and displays the value of the
X-Request-Id in the response header.

Usage:
    ./script.py <URL>
"""
import requests
import sys


def fetch_x_request_id(url):
    """
    Sends a request to the URL and displays the X-Request-Id header value.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

if __name__ == "__main__":
    fetch_x_request_id(sys.argv[1])
