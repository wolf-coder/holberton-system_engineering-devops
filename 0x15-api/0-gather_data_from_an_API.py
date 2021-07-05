#!/usr/bin/python3
"""
0. Gather data from an API
"""

import requests
import sys


def Getdata(ID):
    """
    Method that takes the ID number as argument and Displays
    information about it.
    """
    ID = sys.argv[1]
    Done = 0
    DoneTasks = []
    total_task = 0
    url_user = "https://jsonplaceholder.typicode.com/users/" + ID
    res = requests.get(url_user).json()
    name = res.get('name')
    re = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for i in re:
        if i.get('userId') == int(ID):
            if i.get('completed'):
                DoneTasks.append(i['title'])
                Done += 1
            total_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, Done, total_task))
    for x in DoneTasks:
        print("\t {}".format(x))


if __name__ == "__main__":
    Getdata(sys.argv[1])
