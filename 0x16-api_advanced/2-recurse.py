#!/usr/bin/python3
"""
Module 2-recursive.py
Get subreddit recursive
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        consume reddit api by subreddit recursive
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    url2 = '{}?after={}'.format(url, after)
    req = requests.get(url2, headers={'User-Agent': 'ilasso'},
                       allow_redirects=False)
    if req.ok:
        for i in req.json().get('data').get('children'):
            hot_list.append(i.get('data').get('title'))
        after = req.json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
