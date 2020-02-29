import requests
from bs4 import BeautifulSoup
import getpass

BASE_URL = "https://moneyforward.com/"

# セッション開始
session = requests.session()

loginUser = input("ID:")
loginPass = getpass.getpass("PASS:")  # 入力文字をprintしない

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

# print(soup.get_text)

token = soup.find_all("input",{"name":"authenticity_token"})
loginInfo["authenticity_token"] = token[0].get("value")

for key,value in loginInfo.items():
    print("{0} {1}".format(key,value))

# ログイン先のHTMLを取得
resLogin = session.post(
    BASE_URL+"/session",
    params=loginInfo)
resLogin.raise_for_status()

soupLogin = BeautifulSoup(resLogin.text,"html.parser")
print(soupLogin.get_text)
