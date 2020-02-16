import requests
from bs4 import BeautifulSoup

BASE_URL = "https://uta.pw/sakusibbs/"
USER = "testKen"
PASS = "testKen"

# セッション開始
session = requests.session()

# input ~~~  name の部分。postでログイン情報をサーバーに送っている部分
login_info = {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS,
    "back":"index.php",
    "mml_id":"0"
}

# アクション htmlの「form action ・・・」の部分かな
urlLogin = BASE_URL + "users.php?action=login&m=try"

# ログイン先のHTMLを取得
res = session.post(urlLogin, params=login_info)   # data= だとダメだったので、params= に書き換えたらOKだった(?)
res.raise_for_status()

soup = BeautifulSoup(res.text,"html.parser")
loginText = soup.select(".islogin a")   # isloginというclass属性を抽出。class属性とは要素にクラス名を指定する
                                        # クラス名はCSSの目印であるセレクタとして使われる
                                        # selectメソッド：セレクタを引数。二つ書いたら＆っぽい
print(loginText)
if loginText == []:
    print("login Failure")
    quit()

