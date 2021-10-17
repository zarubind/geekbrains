# 1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о
# письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172???

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pymongo import MongoClient

def write_to_db(data):
    client = MongoClient('127.0.0.1', 27017)
    db = client['emails']
    mail_ru = db.mail_ru
    for item in data:
        if mail_ru.count_documents(item) == 0:
            mail_ru.insert_one(item)

def parse_msg(link):
    driver.get(link)
    try:
        wait = WebDriverWait(driver, 10)
        button_wait = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'letter__date')))
        msg_info = {
            'link': link,
            'sender': driver.find_element_by_class_name('letter-contact').get_attribute('title'),
            'subj': driver.find_element_by_class_name('thread__subject').text,
            'date': driver.find_element_by_class_name('letter__date').text,
            'full_text': driver.find_element_by_class_name('letter__body').text
        }
        return msg_info
    except:
        parse_msg(link)

chrome_options = Options()
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
url = 'https://account.mail.ru/'

with open('passwd', 'r') as file:
    login, password = file.read().split()

driver.get(url)
time.sleep(2)
username = driver.find_element_by_name('username')
username.send_keys(login)
username.send_keys(Keys.ENTER)

time.sleep(1)
password_el = driver.find_element_by_name('password')
password_el.send_keys(password)
password_el.send_keys(Keys.ENTER)

time.sleep(6)
links = set()
while True:
    flag = len(links)
    try:
        wait = WebDriverWait(driver, 10)
        button_wait = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
    except: continue
    messages_list = driver.find_element_by_class_name('dataset__items')
    messages = messages_list.find_elements_by_tag_name('a')
    for message in messages:
        link = message.get_attribute('href')
        if (link is not None) and ('e.mail' in link):
            links.add(link)
    if flag == len(links): break
    actions = ActionChains(driver)
    actions.move_to_element(messages[-1])
    actions.perform()

msg_list = []
for link in links:
    msg_list.append(parse_msg(link))

pprint(msg_list)
write_to_db(msg_list)

driver.close()
