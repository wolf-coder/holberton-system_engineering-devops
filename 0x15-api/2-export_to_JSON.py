#!/usr/bin/python3
"""
script to export data in the Json format.
"""
import json
import requests
import sys


def To_Json(ID):
    """
    _Extend your Python script to export data in the JSON format.
    _Requirements:
    *Records all tasks that are owned by this employee
    *Format must be: {
         "USER_ID": [{"task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS,
         "username": "USERNAME"},
         {"task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS,
         "username": "USERNAME"},
         ... ]}
    *File name must be: USER_ID.json
    """

    ID = sys.argv[1]
    Users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(ID)).json()
    TODO = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()

    with open("{}.json".format(ID), "w") as U_ID:
        json.dump({ID: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': Users.get('username')
            } for task in TODO]}, U_ID)


if __name__ == "__main__":
    To_Json(sys.argv[1])
