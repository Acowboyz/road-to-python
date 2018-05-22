import urllib.request
import urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

formdata = {
    "start": "0",
    "limit": "1"
}

data = urllib.parse.urlencode(formdata).encode("utf-8")

request = urllib.request.Request(url, data=data, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))