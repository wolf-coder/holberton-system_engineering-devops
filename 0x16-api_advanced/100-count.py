#!/usr/bin/python3
"""
recursive function.
"""
import re
import requests
headers = {'user-agent': 'ubuntu:hbtn:v1.0\
 (by /u/Brandixitor)'}


def count_words(subreddit, word_list, after='', occurs={}):
    """
    Write a recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """
    url = "https://api.reddit.com/r/{}?limit=100&after={}".\
        format(subreddit, after)
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
    except Exception:
        return
    if (str(response.status_code) == '404'):
        return
    Data_Len = len(data['data']['children'])
    if (Data_Len is 0):
        return
    for i in range(0, Data_Len):
        try:
            GetTitle = data['data']['children'][i]['data']['title']
            for a in word_list:
                try:
                    occurs[a]
                except KeyError:
                    occurs[a] = 0
                finally:
                    occurs[a] += re.subn(r'(?i)(?<!\S)\b{}\b(?!\S)'.format(a),
                                         '', GetTitle)[1]
        except Exception:
            pass
    ValNext = data['data']['after']
    if (ValNext is not None):
        return count_words(subreddit, word_list, ValNext, occurs)
    else:
        for key in sorted(occurs, key=lambda k: (-occurs[k], k)):
            if (occurs[key] > 0):
                print("{}: {}".format(key, occurs[key]))
        return
