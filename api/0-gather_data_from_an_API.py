#!/usr/bin/python3
"""Write a Python script that, using this REST API,
 for a given employee ID, returns information
 about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    n = int(argv[1])

    res_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{n}")
    data_user = res_user.json()

    res_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    data_tasks = res_tasks.json()

    completed_tasks = []
    total_tasks = 0
    done_tasks = 0

    for task in data_tasks:
        if task["userId"] == n:
            total_tasks += 1
            if task["completed"]:
                done_tasks += 1
                completed_tasks.append(task["title"])

    print(f"Employee {data_user['name']} has completed tasks "
          f"({done_tasks}/{total_tasks}):")

    for task_title in completed_tasks:
        print(f"\t {task_title}")
