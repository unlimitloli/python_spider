import urllib.request as request
import urllib.parse as parse
import urllib.error
import http.cookiejar

is_init = False
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'


def request_url(url, data={}, encode='utf-8'):
    postdata = parse.urlencode(data).encode(encode)
    req = request.Request(url, postdata)
    req.add_header('User-Agent', agent)
    try:
        reqdata = request.urlopen(req)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print('error code: ', e.code)
        if hasattr(e, 'reasn'):
            print('error reasen: ', e.reason)
    return reqdata


def request_url_file(url, filename='', data={}, encode='utf-8'):
    data = request_url(url, data, encode)
    with open(filename, 'wb') as file:
        file.write(data.read())


def init():
    if is_init:
        return

    httphd = request.HTTPHandler(debuglevel=1)
    httpshd = request.HTTPSHandler(debuglevel=1)
    cookie = request.HTTPCookieProcessor(http.cookiejar.CookieJar())
    opener = request.build_opener(httphd, httpshd, cookie)
    request.install_opener(opener)

init()
