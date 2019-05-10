import urllib.request as request
import urllib.parse as parse

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
header = ('User-Agent', agent)

url = 'https://www.iqianyue.com/mypost'
postdata = parse.urlencode({
    'name': 'sjy',
    'pass': '123',
}).encode('utf-8')

req = request.Request(url, postdata)
req.add_header('User-Agent', agent)
data = request.urlopen(req)

with open('post.html', 'wb') as file:
    file.write(data.read())
