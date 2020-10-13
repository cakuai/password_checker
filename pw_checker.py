#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests  # 建立各種 HTTP 請求，從網頁伺服器上取得想要的資料。
import sys
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    # data fr. https://haveibeenpwned.com/API/v3
    # 此ＡＰＩ的功能可回傳所有以 該5字 開頭的password及被leak的次數
    res = requests.get(url)
    if res.status_code != 200:  # 對該ＡＰＩ而言 200才代表正常運行
        raise RuntimeError(
            f"Here's the Error: , check the API and try again")
    return res


def pwned_api_check(password):
    # check whether or not the password exists in API response
    # hexidigest 用來轉成16進位
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return sha1password


print(pwned_api_check("123"))
