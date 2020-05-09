#!/usr/bin/python3
"""
Module 0-subs.py
Get subreddit subscribers
"""

import requests


def top_ten(subreddit):
    """
        consume reddit api by subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'ilasso'},
                       params={'limit': 10}, allow_redirects=False)
    if req.ok:
        for i in req.json().get('data').get('children'):
            print(i.get('data').get('title'))
    else:
        print(None)
    return 0
