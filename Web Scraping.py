import pandas as pd
import requests as r
from bs4 import BeautifulSoup

ws=r.get('https://blinkit.com/cn/fiction-books/cid/1559/274').text
print(ws)

v = BeautifulSoup(ws, 'html.parser')
y=v.find_all('img')
adding_a_tag=[]
for i in y:
    print(i.get('src'))

