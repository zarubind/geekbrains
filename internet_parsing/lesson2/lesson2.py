# Вариант 1
# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем
# должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц
# сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть
# одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в
# json либо csv.

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from pprint import pprint

# https://krasnoyarsk.hh.ru/search/vacancy?clusters=true&ored_clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=Python&page=0
find_text = 'Python'
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
            salary_from = salary_split[1]
            currency = salary_split[2].replace('.', '')
        elif salary.find('до') != -1:
            salary_to = salary_split[1]
            currency = salary_split[2].replace('.', '')
        else:
            salary_from = salary_split[0]
            salary_to = salary_split[2]
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

next_url = url
vacancy_list = []
while next_url:
    response = requests.get(next_url, headers=headers)
    vacancy_list += parse_page(response)
pprint(vacancy_list)
print(len(vacancy_list))

pd.DataFrame(vacancy_list).to_csv('vacancy.csv', index=False)
