#!/usr/bin/python3
"""
Export all users all tasks data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    # get all users
    urlalluser = 'https://jsonplaceholder.typicode.com/users/'
    respalluser = requests.get(urlalluser)
    useralldict = respalluser.json()
    for i in useralldict:
        urluser = 'https://jsonplaceholder.typicode.com/users/{}' \
                  .format(i.get('id'))
        respuser = requests.get(urluser)
        resptask = requests.get('https://jsonplaceholder.typicode.com/todos/',
                                params={'userId': i.get('id')})
        taskdict = resptask.json()
        userdict = respuser.json()

        lista = []
        try:
            if dicttot:
                pass
        except NameError:
            dicttot = {}

        for j in taskdict:
            dictionary = {}
            dictionary['username'] = userdict.get('username')
            dictionary['task'] = j.get('title')
            dictionary['completed'] = j.get('completed')
            lista.append(dictionary)
        dicttot[i.get('id')] = lista

    with open("todo_all_employees.json", "w+") as file:
        json.dump(dicttot, file)
