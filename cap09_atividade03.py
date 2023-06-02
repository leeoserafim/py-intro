from requests import get
from bs4 import BeautifulSoup
from os import system, name
import re

system('cls') if (name == 'nt') else system('clear')

url='https://chromedriver.chromium.org/downloads'

response=get(url)

# print(response.status_code)

html_soup= BeautifulSoup(response.text, 'html.parser')

tags=html_soup.find_all('ul')

for i in range(len(tags)):
    if(tags[i].text.find('you are using Chrome version')>0):
        listas=tags[i].find_all('li')
        print(listas, '\n\n')
        if(len(listas)>=1):
            print(listas[0].text)
            print(listas[0].text[-13:])
            url_download='https://chromedriver.storage.googleapis.com/' + listas[1].text[-13:] + '/chromedriver_win32.zip'
            print(url_download)

