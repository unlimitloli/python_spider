import urllib.request as request

httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httphd, httpshd)
request.install_opener(opener)
data = request.urlopen('http://blog.csdnn.net')

with open('csdnn.html', 'wb') as file:
    file.write(data.read())
