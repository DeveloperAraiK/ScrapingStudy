import requests
from bs4 import BeautifulSoup

BASE_URL = "https://uta.pw/sakusibbs/"
USER = "testKen"
PASS = "testKen"

# セッション開始
session = requests.session()

# <form action … のelement全体の中から、nameの部分を抽出。postでログイン情報をサーバーに送っている部分
login_info = {
    "username_mmlbbs6":USER,    # value は空っぽ
    "password_mmlbbs6":PASS,
    "back":"index.php",         # value が index.php
    "mml_id":"0"                # value が 0
}

# アクション htmlの「form action ・・・」の部分かな
urlLogin = BASE_URL + "users.php?action=login&m=try"

# ログイン先のHTMLを取得
res = session.post(urlLogin, params=login_info)   # data= だとダメだったので、params= に書き換えたらOKだった(?)
res.raise_for_status()

soup = BeautifulSoup(res.text,"html.parser")
loginText = soup.select(".islogin a") 
    # isloginというclass属性を抽出。class属性とは要素にクラス名を指定する
    # クラス名はCSSの目印であるセレクタとして使われる
    # selectメソッド：セレクタ指定→ドットを書く。タグもかける？＆になるっぽい
# print(loginText)
if loginText == []:
    print("login Failure")
    quit()

# 参考１）
# for i in soup.find_all("a"):  # aタグがリストで取得されるのでforで取り出す
#     print(i.get("href"))

# 参考２）
# z = soup.select("#header_menu_linkbar")   # selectメソッド：ID指定→#つける

# マイページリンクの取得 href属性のユーザーパラメーターとの組み合わせでリンクURL担っている
user = loginText[0].get("href")     # loginTextは要素数１個のリストなので、１要素目に対してget
myPageLink = BASE_URL + user
print(myPageLink)

res = session.get(myPageLink)       # マイページのHTML取得
res.raise_for_status()
mySoup = BeautifulSoup(res.text,"html.parser")
print(mySoup.get_text())