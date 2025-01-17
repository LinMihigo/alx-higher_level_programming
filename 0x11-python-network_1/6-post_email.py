#!/usr/bin/python3
"""
A script that sends a POST request to a URL with the email as a parameter
and displays the body of the response.

Usage:
    ./script.py <URL> <email>
"""
import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to send as a parameter.
    """
    response = requests.post(url, data={'email': email})
    print(response.text)


if __name__ == "__main__":
    send_post_request(sys.argv[1], sys.argv[2])
