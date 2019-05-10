import urllib.request as request
import os

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
header = ('User-Agent', agent)

key = 'hello'
url = 'http://www.baidu.com/s?wd=' + key
request.urlretrieve(url, 'baidu.html')
request.urlcleanup()