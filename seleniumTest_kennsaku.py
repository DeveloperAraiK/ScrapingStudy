from selenium import webdriver
import chromedriver_binary 
import time

browser = webdriver.Chrome()
browser.get("https://www.google.com/")

# 入力が完了する前に検索ボタンを押してしまうとエラーが生じるため時間を置かせる
time.sleep(3) # sec

# 検索欄に任意の文字を入力
search = browser.find_element_by_name("q")
search.send_keys("マネーフォワード")

# 検索ボタンをクリック
time.sleep(3) # sec
button = browser.find_element_by_class_name("gNO89b")
button.click()
