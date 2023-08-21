#!/usr/bin/python3

import requests
from sys import argv
import csv

if __name__ == "__main__":

    n = int(argv[1])

    res_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{n}")
    data_user = res_user.json()

    res_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    data_tasks = res_tasks.json()

    _tasks = 0
    realized = 0
    completed_tasks = []

    for tasks in data_tasks:
        if tasks["userId"] == n:
            if tasks["completed"] is True:
                completed_tasks.append(tasks["title"])
                realized += 1

            else:
                _tasks += 1

            _tasks += realized

    print(f"Employee {data_user['name']} is done with tasks"
          f"({realized}/{_tasks}):")
    for task_title in completed_tasks:
        print(f"\t {task_title}")

    filename = f"{n}.csv"
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for tasks in data_tasks:
            if tasks["userId"] == n:
                USER_ID = str(tasks["userId"])
                USERNAME = data_user["username"]
                TASK_COMPLETED_STATUS = str(tasks["completed"])
                TASK_TITLE = tasks["title"]

                f.write('"{}", "{}", "{}", "{}"\n'.format(USER_ID, USERNAME,
                        TASK_COMPLETED_STATUS,  TASK_TITLE))
