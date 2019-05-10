import urllib.request as request

file = request.urlopen('http://www.baidu.com')
data = file.read();
print(data)