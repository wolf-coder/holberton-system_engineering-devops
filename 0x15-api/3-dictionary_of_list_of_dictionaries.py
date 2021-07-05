#!/usr/bin/python3
"""
script to export data in the Json format.
"""
import json
import requests
import sys


def To_ListOfFDict():
    """
    _Script to export data in the JSON format.
    _Requirements:
        *Records all tasks from all employees
        *Format must be: { "USER_ID": [ {"username": "USERNAME",
             "task": "TASK_TITLE",
             "completed": TASK_COMPLETED_STATUS},
             {"username": "USERNAME",
             "task": "TASK_TITLE",
             "completed": TASK_COMPLETED_STATUS},
             ... ],
             "USER_ID": [ {"username": "USERNAME",
             "task": "TASK_TITLE",
             "completed": TASK_COMPLETED_STATUS},
             {"username": "USERNAME",
             "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
        *File name must be: todo_all_employees.json
    """

    FileName = "todo_all_employees.json"
    r_id = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open(FileName, "w") as File:
        d = {elem.get("id"): [{'task': y.get('title'),
             'completed': y.get('completed'),
                               'username': elem.get('username')} for y in r
                              if elem.get("id") == y.get('userId')]
             for elem in r_id}
        json.dump(d, File)


if __name__ == "__main__":
    To_ListOfFDict()
