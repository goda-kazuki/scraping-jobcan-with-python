from dotenv import load_dotenv
import os
load_dotenv(override=True)  # overrideで既存の環境変数があっても上書き


print(os.environ.get("USER_EMAIL"))
print(os.environ.get("USER_PASSWORD"))

#
#
#
# import requests
# from bs4 import BeautifulSoup
# # Webページを取得して解析する
#
# load_url = "https://id.jobcan.jp/users/sign_in"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")
#
# print(soup)
# name="user[email]"
# name="user[password]"
# action="/users/sign_in"
# method="post"
