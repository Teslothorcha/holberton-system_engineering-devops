#!/usr/bin/python3
""" using this REST API,
to gather info about employee"""

import requests
import sys

if __name__ == "__main__":
    parameters_t = (('userId', sys.argv[1]),)
    to_dos = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params=parameters_t)
    to_dos_j = to_dos.json()

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    user_j = user.json()
    user_name = user_j['name']

    completed_list = []
    for maybe in to_dos_j:
        if maybe['completed'] is True:
            completed_list.append(maybe)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        len(completed_list),
        len(to_dos_j)))
    for title in completed_list:
        print("\t {}".format(title['title']))
