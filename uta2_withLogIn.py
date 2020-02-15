import requests
from bs4 import BeautifulSoup

BASE_URL = "https://uta.pw/sakusibbs/"
USER = "testKen"
PASS = "testKen"

session = requests.session()

login_info = {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS,
    "back":"index.php",
    "mml_id":"0"
}

# アクション？ htmlの「form action ・・・」の部分かな
urlLogin = BASE_URL + "users.php?action=login&m=try"    
res = session.post(urlLogin, params=login_info)   # data= だとダメだったので、params= に書き換えたらOKだった
res.raise_for_status()
print(res.text)

