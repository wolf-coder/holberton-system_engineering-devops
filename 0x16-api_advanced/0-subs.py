#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers.
"""
import json
import requests


def number_of_subscribers(subreddit):
    Data = {"User-Agent": "Ahmed_belhaj"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=Data)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
