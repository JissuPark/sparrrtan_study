
import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
  ' h3 > a '
)
data = {}

for title in my_titles:
   data[title.text] = title.get('href')
   print(data[title.text])
with open(os.path.join(BASE_DIR, 'result.json'), 'w+',encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent="\n")




