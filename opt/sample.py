from dotenv import load_dotenv
import os
load_dotenv(override=True)  # overrideで既存の環境変数があっても上書き

import requests
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# セッションを開始
session = requests.session()

# load_url = "https://ssl.jobcan.jp/login/pc-employee-global?err=1&lang_code="
# html = session.get(load_url)
# soup = BeautifulSoup(html.content, "html.parser")

# authenticity_token = soup.find(attrs={'name':'authenticity_token'}).get('value')


# ログイン
login_info = {
    "email":os.environ.get("USER_EMAIL"),
    "password":os.environ.get("USER_PASSWORD"),
    "client_id":os.environ.get("CLIENT_ID"),
    "save_login_info":"0",
    "url":"/pc-employee-global",
    "login_type":"1",
    "lang_code":"ja"

#     "commit":"ログイン",
#     "authenticity_token":authenticity_token,
#     "user[client_code]":""
}

# action
url_login = "https://ssl.jobcan.jp/login/pc-employee-global?err=1&lang_code="
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)
