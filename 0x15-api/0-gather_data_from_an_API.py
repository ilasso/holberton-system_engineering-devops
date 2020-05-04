#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':

    Qdone = 0
    Qtotal = 0

    urluser = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    respuser = requests.get(urluser)
    userdict = respuser.json()
    username = userdict.get('name')

    resptask = requests.get('https://jsonplaceholder.typicode.com/todos/',
                            params={'userId': argv[1]})

    completed = []
    for i in resptask.json():
        if i.get('completed') is True:
            completed.append(i.get('title'))
            Qdone = Qdone + 1
        Qtotal = Qtotal + 1
    emplheader = "Employee {} is done with task {}/{}:".format(username,
                                                               Qdone, Qtotal)
    print(emplheader)
    display = "\t " + "\n\t ".join(completed)
    print(display)
