import urllib.request
import urllib.parse


url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

key = input("需要翻譯的字:")

headers = {
    # "Host" : "fanyi.youdao.com",
    # "Connection" : "keep-alive",
    # "Content-Length" : "201",
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With" : "XMLHttpRequest"
    # "Accept-Language" : "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4"
}

# %s/\(.*\)=\(.*\)$/"\1" : "\2",/g
formdata = {
    "i" : key,
    "from" : "AUTO",
    "to" : "AUTO",
    "smartresult" : "dict",
    "client" : "fanyideskweb",
    # "salt" : "1526896142741",
    # "sign" : "1b4f47d16b243c8f9caef0615b9b1841",
    "doctype" : "json",
    "version" : "2.1",
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_REALTIME",
    "typoResult" : "false"
}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}

data = urllib.parse.urlencode(formdata).encode("utf-8")

requset = urllib.request.Request(url, data=data, headers=headers)

response = urllib.request.urlopen(requset).read().decode("utf-8")

print(response)

