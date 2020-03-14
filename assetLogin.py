import requests
from bs4 import BeautifulSoup
import getpass
import myLib

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

resp = session.get(BASE_URL+"/users/sign_in")
soup = BeautifulSoup(resp.content,"html.parser")

# token取得
# for key,value in loginInfo.items():
#     print("{0} {1}".format(key,value))
 # パスワード、google、Facebookを使ってログインなどがあるので
 # それぞれにtokenが設定されている。とりあえず全部取り出す
token = soup.find_all("input",{"name":"authenticity_token"})
 # パスワードでログインのtokenは1個目
loginInfo["authenticity_token"] = token[0].get("value")

# ログイン後トップページのHTMLを取得
resTop = session.post(
    BASE_URL+"/session",
    params=loginInfo)
resTop.raise_for_status()

soupTop = BeautifulSoup(resTop.text,"html.parser")
# print(soupTop.find_all("a"))
print(soupTop.get_text)
