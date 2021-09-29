# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import os
import requests

repos = requests.get('https://api.github.com/users/zarubind/repos?per_page=1000')
for i in repos.json():
    print(i['name'])
#print(repos.json())
with open('1.txt', 'w') as file:
    file.write(repos.text)

# 2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

username = 'user'
token = 'xxxxxx'
repos = requests.get('https://api.github.com/user', auth=(username, token))
with open('2.txt', 'w') as file:
    file.write(repos.text)
