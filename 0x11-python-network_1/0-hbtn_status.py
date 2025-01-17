#!/usr/bin/python3
"""
A script that fetches a given URL using the `urllib` package.

Usage:
    ./0-hbtn_status.py | cat -e
"""
import urllib.request


def fetch_url_status(url):
    """
    Fetches and displays the status of a URL.

    Args:
        url (str): The URL to fetch.
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_url_status("https://alx-intranet.hbtn.io/status")
