# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости
# (https://yandex.ru/news/). Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные данные в БД
# Минимум один сайт, максимум - все три

from lxml import html
import requests
from pprint import pprint
from pymongo import MongoClient

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
url = 'https://news.mail.ru/'

def write_to_db(data):
    client = MongoClient('127.0.0.1', 27017)
    db = client['news']
    mail_ru = db.mail_ru
    for item in data:
        if mail_ru.count_documents(item) == 0:
            mail_ru.insert_one(item)

response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)
links = dom.xpath("//table[@class='daynews__inner']//a[contains(@class, 'photo')]/@href") + \
        dom.xpath("//li[@class='list__item']/a[@class='list__text']/@href")
news_list = []
for link in links:
    response = requests.get(link, headers=headers)
    dom = html.fromstring(response.text)
    src = dom.xpath("//span[@class='note']//span[@class='link__text']/text()")
    name = dom.xpath("//h1/text()")
    date = dom.xpath("//span[@class='note']/span/@datetime")
    news_list.append({
        'src': src[0],
        'name': name[0],
        'link': link,
        'date': date[0]
    })

write_to_db(news_list)
pprint(news_list)
print(len(news_list))
