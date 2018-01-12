# -*- coding:utf-8 -*-
# import urllib.request, sys,base64,json,os,time,pyperclip,
import baiduSearch
from PIL import Image
import time
import sys
import os
from aip import AipOcr

reload(sys)
sys.setdefaultencoding('utf8')

os.chdir('E:/hxj/million hero/WD-Helper-master/WD-Helper-master/atq/src')

# 百度OCR信息，使用自己注册的即可
APP_ID = '***'
API_KEY = '***'
SECRET_KEY = '***' 


def autoChoose():
    start_time = time.time()
    # screencap and  pull
    os.system('adb shell screencap -p /sdcard/screen_shot.png')
    os.system('adb pull /sdcard/screen_shot.png .')

    # crop image
    image = Image.open('./screen_shot.png')
    image_size = image.size
    print image_size
    width = image_size[0]
    height = image_size[1]
    region = image.crop((0, height * 0.15, width, height * 0.7))
    region.save('./screen_shot_crop.png')
    # OCR
    aa = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    filepath = './screen_shot_crop.png'
    with open(filepath, 'rb') as fp:
        image = fp.read()
    ret = aa.basicGeneral(image)

    # question region
    if ret:
        ask = ''
        lines = ret['words_result']


        if len(lines) <= 4:
            ask = lines[0]['words'].split('.')[-1]

        elif len(lines) == 5:
            ask = lines[0]['words'].split('.')[-1]  + lines[1]['words']

        elif len(lines) > 5:
            ask = lines[0]['words'].split('.')[-1] + lines[1]['words'] + lines[2]['words']

    if len(lines) >= 3:
        Coption = lines[-1]['words']
        Boption = lines[-2]['words']
        Aoption = lines[-3]['words']
    else:
        Aoption, Boption, Coption = ' ', ' ', ' '

    keyword = ask
    print keyword
	
    convey = 'n'
    end_time = time.time()
    if convey == 'y' or convey == 'Y':
        results = baiduSearch.search(keyword, convey=True)
    elif convey == 'n' or convey == 'N' or not convey:
        results = baiduSearch.search(keyword)
    else:
        print('输入错误')
        exit(0)
    count = 0

    N = {'A': 0, 'B': 0, 'C': 0}

    for result in results:

        N['A'] += result.abstract.count(Aoption)
        N['B'] += result.abstract.count(Boption)
        N['C'] += result.abstract.count(Coption)
        # Qred = result.abstract.replace(keyword, '\033[1;30;41m' + keyword + '\033[0m')# '\033[1;30;41m' + Aoption + '\033[0m'
        Ared = result.abstract.replace(Aoption, '\033[1;31m' + Aoption + '\033[0m')#'\033[1;30;41m' + Aoption + '\033[0m'
        Bred = Ared.replace(Boption, '\033[1;32m' + Boption + '\033[0m')#'\033[1;32m' + 'Boption' + '\033[0m'
        Cred = Bred.replace(Coption, '\033[1;34m' + Coption + '\033[0m')#'\033[1;34m' + 'Coption' + '\033[0m'

        print('\033[1;30;41m' + result.title + '\033[0m')
        print ' '
        print Cred
        print ' '
        count = count + 1
        if count == 4:
            break
    print '\033[1;31;40m','答案： ',max(N.items(), key=lambda x: x[1])[0], '\033[0m'


    print(r'run time: ' + str(end_time - start_time) + 's')


if '__main__' == __name__:
    while True:
        mode = raw_input(
            "Menu:--\n1:Choose Answer 1;\n2:Choose Answer 2;\n3:Choose Answer 3;\n4:Random Answer\n5:Auto Analysis\n")
        if mode == '5':
            autoChoose()
        else:
            print 'unknown'
