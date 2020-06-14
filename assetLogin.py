#############################
# requestsを使ってマネーフォワードにログインする
# note:
# ログイン方法が変わって、ログインできない状態
#############################
import requests
from bs4 import BeautifulSoup
import getpass
import myLib
import sys

BASE_URL = "https://moneyforward.com/"

# セッション開始
session = requests.session()

# ID/Pass取得
idpass = myLib.get_id_pass()
if idpass[0] != "":
    loginUser = idpass[0]
    loginPass = idpass[1]
else:
    # ファイルにID/Passが設定されていなかったらコンソール入力
    loginUser = input("ID:")
    loginPass = getpass.getpass("PASS:")  # 入力Passはprint文出さない

# ログイン情報
loginInfo = {
    "utf8":"✓",
    "authenticity_token":None,
    "sign_in_session_service[email]":loginUser,
    "sign_in_session_service[password]":loginPass,
    "new1":"1",
    "commit":"ログイン"
}

# userAgent ブラウザとして HTTP Getする
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "\
                 "AppleWebKit/537.36 (KHTML, like Gecko) "\
                 "Chrome/81.0.4044.129 Safari/537.36 "
resp = session.get(BASE_URL+"/users/sign_in", headers={"User-Agent": ua})

# リダイレクトを確認(あんまり意味はない。勉強のため)
# -O オプションで実行すると実行するif文
if not __debug__:
    print("loginPage Get")
    print("    - status_code:{0}".format(resp.status_code)) # 200=成功(リダイレクトは3XXだが最終的な結果?)
    print("    - Redirect url:{0}".format(resp.url)) # ブラウザで確認できるURLのと同じのが入っている
    print("    - history len:{0}".format(len(resp.history))) # 4回リダイレクトされているっぽい

soup = BeautifulSoup(resp.content,"html.parser")

sys.exit()
# これ以降はサイトのログイン方式変更前のコード

# token取得
# for key,value in loginInfo.items():
#     print("{0} {1}".format(key,value))
 # パスワード、google、Facebookを使ってログインなどがあるので
 # それぞれにtokenが設定されている。とりあえず全部取り出す
token = soup.find_all("input",{"name":"authenticity_token"})
 # パスワードでログインのtokenは1個目
loginInfo["authenticity_token"] = token[0].get("value")

# ログイン
ses = session.post(
    BASE_URL+"/session",
    params=loginInfo)
ses.raise_for_status()

# ↓↓セッション保持できているので、ここからは普通に get できる

# 資産ページ HTML取得
resShisan = session.get(BASE_URL + "bs/portfolio")
resShisan.raise_for_status()
ses = BeautifulSoup(resShisan.text,"html.parser")

total = ses.find_all(class_="bs-total-assets")
print(total[0].find_all(class_="table table-bordered"))
# kabushiki = ses.find_all(class_="table table-bordered table-eq")

# print(kabushiki[0])

# trs = kabushiki.find_all("tr")
# print(trs)

# for i in kabushiki:
#     print(i.find_all("tr"))
# print(kabushiki[0].find_all("tr"))
