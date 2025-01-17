#!/usr/bin/python3
"""
A script that sends a POST request with a letter as a parameter to
a url and displays the id and name from the JSON response.

Usage:
    ./script.py <letter>
"""
import requests
import sys


def search_user(letter):
    """
    Sends a POST request to the search_user endpoint with the letter
    as a parameter.

    Args:
        letter (str): The letter to send as a parameter.
    """
    response = requests.post(
        'http://0.0.0.0:5000/search_user',
        data={'q': letter}
    )

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user(sys.argv[1] if len(sys.argv) > 1 else "")
