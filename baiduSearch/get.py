# -*- coding:utf-8 -*-
import requests

__url =  'https://zhidao.baidu.com/search?word='  # 搜索请求网址


def page(word):
    r = requests.get(__url + word)
    r.encoding = 'gbk'
    if r.status_code == 200:  # 请求错误（不是200）处理
        return r.text
    else:
        print(r.status_code)
        return False


