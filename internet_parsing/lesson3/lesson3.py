# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные
# вакансии в созданную БД.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.
# 3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.

from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from pprint import pprint

# https://krasnoyarsk.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=Python&page=0
find_text = 'qgis'
site = 'https://krasnoyarsk.hh.ru'
url = 'https://krasnoyarsk.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=' + find_text
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}

def parse_salary(salary):
    salary_from = None
    salary_to = None
    currency = None
    if salary:
        salary_split = salary.split()
        if salary.find('от') != -1:
            salary_from = int(salary_split[1])
            currency = salary_split[2].replace('.', '')
        elif salary.find('до') != -1:
            salary_to = int(salary_split[1])
            currency = salary_split[2].replace('.', '')
        else:
            salary_from = int(salary_split[0])
            salary_to = int(salary_split[2])
            currency = salary_split[3].replace('.', '')
    return [salary_from, salary_to, currency]

def parse_page(response):
    global next_url
    data_to_return = []
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.find_all('div', {'class': 'vacancy-serp-item'})
    for vacancy in vacancy_list:
        v_info = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
        v_title = v_info.getText()
        v_url = v_info.get('href')
        v_salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
        v_salary = v_salary.getText().replace('\u202f', '') if v_salary else None
        v_salary = parse_salary(v_salary)
        data_to_return.append({
            "title": v_title,
            "salary_from": v_salary[0],
            "salary_to": v_salary[1],
            "currency": v_salary[2],
            "url": v_url,
            "site": next_url
            })
    next_url = soup.find('a', {'data-qa': 'pager-next'})
    next_url = site + next_url.get('href') if next_url else None
    return data_to_return

def write_to_db(data):
    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancies']
    hhru = db.hhru
    for item in data:
        if hhru.count_documents(item) == 0:
            hhru.insert_one(item)

def print_gt_vacancy(salary):
    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancies']
    hhru = db.hhru
    for item in hhru.find({'$or': [{'salary_from': {'$gt': salary}},
                                   {'salary_to': {'$gt': salary}}]}):
        pprint(item)

next_url = url
vacancy_list = []
while next_url:
    response = requests.get(next_url, headers=headers)
    vacancy_list += parse_page(response)
pprint(vacancy_list)
print(len(vacancy_list))

write_to_db(vacancy_list)
print('\n\n\n--------------------------------\n\n\n')
print_gt_vacancy(80000)

# pd.DataFrame(vacancy_list).to_csv('vacancy.csv', index=False)
