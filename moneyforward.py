#############################
# seleniumを使って、マネーフォワードへ
# note:
#############################
from selenium import webdriver
import chromedriver_binary 
import time
import sys
import getIdPass

loginId,loginPass = getIdPass.GetMoneyForwardIdPass()

browser = webdriver.Chrome()
browser.get("https://moneyforward.com/")

time.sleep(3)
button = browser.find_element_by_class_name("web-sign-in")
button.click() # ログインボタン

time.sleep(3)
# ログイン方法が複数ありclassは全部同じ。classの先頭=メールアドレス
button = browser.find_element_by_class_name("_2sZu7ciR")
button.click() # メールアドレスでログイン

# 検索欄に任意の文字を入力
# search = browser.find_element_by_name("q")
# search.send_keys("マネーフォワード")
