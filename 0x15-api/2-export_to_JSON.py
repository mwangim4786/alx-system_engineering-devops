#!/usr/bin/python3
"""
Exports to-do list information for a given employee to JSON format.
"""

#import json
from json import dump
import requests
import sys


if __name__ == "__main__":

    # URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee ID from the command-line argument
    user_id = sys.argv[1]



    # Get user info using the employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Getthe to_do list for the employee using employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    # Create a dictionary containing the users to_do list information
    data_to_export = {user_id: []}

    for to_do in todos:
        data_to_export[user_id].append({"task": to_do.get("title"),
	                                "completed": to_do.get("completed"),
	                                "username": username})

    #data_to_export[user_id].append(tasks_info)

    # Write the data to a JSON file with employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        dump(data_to_export, jsonfile, indent=4)

