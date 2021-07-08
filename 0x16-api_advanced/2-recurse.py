#!/usr/bin/python3
"""
Get All article of a user
"""
import pprint
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Get All article of a user
    """
    params = {'limit': 100}
    headers = {'User-agent': 'Unix:0-subs:v1'}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get('http://reddit.com/r/{}/hot.json'.
                            format(subreddit),
                            headers=headers,
                            params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
