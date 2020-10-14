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


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count


def pwned_api_check(password):
    # check whether or not the password exists in API response
    # hexidigest 用來轉成16進位
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)  # 回傳的是tails們
    ans = get_password_leak_count(response, tail)
    return ans


def main(args):  # 若不加＊ 就代表他只是一般參數
    for password in args:
        count = pwned_api_check(password)
        if count != 0:  # 表示有被leak
            print(
                f"{password} was found {count} times, please consider a change......")
        else:
            print(f"{password} was NOT FOUND, keep on going")


main(sys.argv[1:])
