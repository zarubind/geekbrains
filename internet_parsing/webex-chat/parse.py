from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from pprint import pprint

def parse_page(response):
    data_to_return = []
    soup = bs(response, 'html.parser')
    message_list = soup.find_all('div', {'class': 'chatItem'})
    for message in message_list:
        msg = message.find('span', {'class': 'itemTimeStamp'})
        msg_time = msg.getText()
        msg_text = message.find('div', {'class': None}).getText()
        msg_user = message.find('strong', {'class': None}).getText()
        data_to_return.append({
            "msg_user": msg_user,
            "msg_time": msg_time,
            "msg_text": msg_text
            })
    return data_to_return

with open("Webex.htm", "r", encoding="utf-8") as file:
    response = file.read()
chat_list = parse_page(response)

pprint(chat_list)
print(len(chat_list))
pd.DataFrame(chat_list).to_csv('chat.csv', index=False, sep='\t')
pd.DataFrame(chat_list).to_excel('chat.xlsx', index=False)
