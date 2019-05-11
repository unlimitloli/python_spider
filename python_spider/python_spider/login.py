from common import *

url1 = 'http://account.chinaunix.net/login/login'
url2 = 'http://bbs.chinaunix.net'
postdata = {
    'username': 's82048764',
    'password': 'hmqst520',
    }

request_url_file(url1, 'china1.html', postdata)
request_url_file(url2, 'china2.html', postdata)

