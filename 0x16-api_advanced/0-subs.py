#!/usr/bin/python3
"""
script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Your User Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:  # Not Found
            return 0
        else:
            return "Error: Unexpected status code"
    except Exception as e:
        return f"Error: {e}"
