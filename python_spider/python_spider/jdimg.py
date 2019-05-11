import urllib.request as request
import urllib.parse as parse
import urllib.error
import re
import os
import sys

list_re = '<div id="plist".+?<div class="page clearfix">'
img_re = re.compile('<img width="\d+" height="\d+" data-img="\d+" (?:(?:src)|(?:data-lazy-img))="//(.+?\.jpg)">')


def down_img(src, page):
    url = src + str(page)
    data = request.urlopen(url).read().decode('utf-8')
    list_data = re.search(list_re, data, re.S)

    try:
        if list_data:
            imgs = img_re.findall(list_data.group())
            count = 0
            for img in imgs:
                img_name = './jbimg/' + str(page) +'_' + str(count) +'.jpg'
                img_url = 'http://' + img
                request.urlretrieve(img_url, img_name)
                count += 1
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print('error code: ', e.code)
        if hasattr(e, 'reasn'):
            print('error reasen: ', e.reason)

src = 'https://list.jd.com/list.html?cat=9987,653,655&page='

if not os.path.exists('./jbimg'):
    os.mkdir('./jbimg')

for i in range(1, 137):
    down_img(src, i)