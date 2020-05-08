#!/usr/bin/python3
"""
Module 0-subs.py
Get subreddit subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
        consume reddit api by subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'ilasso'},
                       allow_redirects=False)
    if req.ok:
        return req.json().get('data').get('subscribers')
    return 0
