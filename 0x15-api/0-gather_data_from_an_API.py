#!/usr/bin/python3
"""
returns information about TODO list progress of a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    # url for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee information frm employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the TO-DO listusing employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Get completed tasks from TO-DO list
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print employee name and number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with tab indentation
    [print("\t {}".format(complete)) for complete in completed]
