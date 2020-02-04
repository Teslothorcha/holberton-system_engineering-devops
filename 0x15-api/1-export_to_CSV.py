#!/usr/bin/python3
import sys
import requests
import csv

"""CSV
"""
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

    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_file:
        cvs_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for to_write in to_dos_j:
            cvs_writer.writerow([int(sys.argv[1]), user_name,
                                to_write['completed'],
                                 to_write['title']])
