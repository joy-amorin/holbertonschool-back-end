#!/usr/bin/python3

"""Write a Python script that, using this REST API,
for a given employee ID, returns
information about his/her TODO list progress."""

import requests
from sys import argv
import csv
import json

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
                _tasks += realized

    print(f"Employee {data_user['name']} is done with tasks"
          f"({realized}/{_tasks}):")
    for task_title in completed_tasks:
        print(f"\t {task_title}")

        """export data in the CSV format."""

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

        """ export data in the JSON format."""

        _filename = f"{n}.json"
        tasks_list = []

    for tasks in data_tasks:
        task_data = {"task": tasks["title"], "completed": tasks["completed"],
                     "username": data_user["username"]}
        tasks_list.append(task_data)
        user_data = {n: tasks_list}

    with open(_filename, "w") as f:
        json.dump(user_data, f)

        """ export data in the JSON format."""

        jason_name = "todo_all_employees.json"
        _task_list = []
        for tasks in data_tasks:
            _task_data = {"username": data_user["username"],
                          "task": tasks["title"],
                          "completed": tasks["completed"]}
            _task_list.append(_task_data)
            _user_data = {n: _task_list}

        with open(jason_name, "w") as f:
            json.dump(_user_data, f)
