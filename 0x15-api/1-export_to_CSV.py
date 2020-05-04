#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':

    urluser = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    respuser = requests.get(urluser)
    userdict = respuser.json()
    username = userdict.get('username')

    resptask = requests.get('https://jsonplaceholder.typicode.com/todos/',
                            params={'userId': argv[1]})
    taskdict = resptask.json()

    lista = []
    listatot = []
    for j in taskdict:
        lista.append(str(argv[1]))
        lista.append(str(userdict.get('username')))
        lista.append(str(j.get('completed')))
        lista.append(str(j.get('title')))
        listatot.append(lista)
        lista = []

    with open("{}.csv".format(argv[1]), "a+") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerows(listatot)
