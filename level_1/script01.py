#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = ' http://158.69.76.135/level1.php'

for i in range(4096):
    s = requests.Session()
    rep = s.get(url)

    soup = BeautifulSoup(rep.text, 'html.parser')
    key = soup.find(type='hidden')["value"]
    my_data = {'id': '3781',
                    'holdthedoor': 'submit',
                    'key': key}

    s.post(url, data=my_data)
