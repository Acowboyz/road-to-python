import urllib.parse
import urllib.request
import random

url = "https://www.baidu.com:443/s"

ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

user_agent = random.choice(ua_list)

keyword = input("請輸入字串:")

wd = {"wd": keyword}

headers = {"User-Agent": user_agent}

wd = urllib.parse.urlencode(wd)

fullurl = url + "?" + wd

# print(fullurl)

request = urllib.request.Request(fullurl, headers=headers)

with urllib.request.urlopen(request) as response:
    html = response.read().decode('utf-8')
    print(html)

