#############################
# RequestsとBeautifulSoupの基本の使い方
# note:
#############################
import requests
from bs4 import BeautifulSoup

r = requests.get("https://uta.pw/")

soup = BeautifulSoup(r.content, "html.parser")

print(soup.text)