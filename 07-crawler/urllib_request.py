import urllib.request

# 加入user-agent
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

request = urllib.request.Request("http://www.baidu.com/", headers = headers)

with urllib.request.urlopen(request) as response:
    html = response.read().decode('utf-8')

    # 返回 http responds
    print(response.getcode())

    # 返回 實際數據的url, 防止重定向問題
    print(response.geturl())

    # 返回 服務器響應 http header
    print(response.info())

# print(html)
