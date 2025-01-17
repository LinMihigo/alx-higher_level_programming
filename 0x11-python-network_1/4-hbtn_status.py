#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status using requests
and displays the body of the response in a specific format.

Usage:
    ./script.py
"""
import requests


def fetch_status(url):
    """
    Fetches and displays the status of a URL.

    Args:
        url (str): The URL to fetch.
    """
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")


if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
