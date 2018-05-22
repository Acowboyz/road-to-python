import urllib.request

response = urllib.request.urlopen("http://www.baidu.com/")
# response = urllib.request.urlopen("https://tieba.baidu.com/f?kw=rng&pn=0")

html = response.read().decode('utf-8')

print(html)
