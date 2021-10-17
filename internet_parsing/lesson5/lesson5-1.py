# 1) Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о
# письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172???

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from pprint import pprint

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
mails = driver.find_elements_by_xpath('//a[@class="llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal"]')
pprint(mails)
mail_list = []
for mail in mails:
    mail.click()
    time.sleep(1)
    mail_list.append({'link': driver.current_url,
                      'sender': driver.find_element_by_class_name('letter-contact').get_attribute('title'),
                      'subj': driver.find_element_by_class_name('thread__subject').text,
                      'date': driver.find_element_by_class_name('letter__date').text,
                      'full_text': driver.find_element_by_class_name('letter-body__body-content').text
                      })
    driver.back()
    time.sleep(1)
    pprint(mail_list)

#for link in mail_list:

# driver.close()
