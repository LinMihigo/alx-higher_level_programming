#!/usr/bin/python3
"""
A script that sends a POST request to a URL with an email as a parameter
and displays the response body decoded in UTF-8.

Usage:
    ./script.py <URL> <email>
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter.

    Args:
        url (str): The URL to send the request to.
        email (str): The email to include as a parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))

if __name__ == "__main__":
    send_post_request(sys.argv[1], sys.argv[2])
