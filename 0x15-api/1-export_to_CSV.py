#!/usr/bin/python3
"""
script to export data in the CSV format.
"""
import csv
import requests
import sys


def To_CSV(ID):
    """
    _Extend your Python script to export data in the CSV format.
    _Requirements:
     *Records all tasks that are owned by this employee
     *Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
     *File name must be: USER_ID.csv

    """
    ID = sys.argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/" + ID).json()
    username = r.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (ID) + '/todos')
    with open("{}.csv".format(ID), "w") as CSVFile:
        writer = csv.writer(CSVFile, quoting=csv.QUOTE_ALL)
        for T in req.json():
            writer.writerow([ID, username,
                            T.get("completed"), T.get("title")])


if __name__ == "__main__":
    To_CSV(sys.argv[1])
