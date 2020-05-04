#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    urluser = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    respuser = requests.get(urluser)
    userdict = respuser.json()
    resptask = requests.get('https://jsonplaceholder.typicode.com/todos/',
                            params={'userId': argv[1]})
    taskdict = resptask.json()

    lista = []
    dicttot = {}
    for j in taskdict:
        dictionary = {}
        dictionary['task'] = j.get('title')
        dictionary['completed'] = j.get('completed')
        dictionary['username'] = userdict.get('username')
        lista.append(dictionary)
    dicttot[argv[1]] = lista

    with open("{}.json".format(argv[1]), "w+") as file:
        file.write(json.dumps(dicttot))
