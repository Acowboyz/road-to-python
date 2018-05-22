import urllib
import urllib.request
import urllib.parse

def loadpage(url, filename):
    """
    根據 url 發送請求, 獲取服務器響應文件
    :param url: 需要爬取的url
    :param filename: 處理的文件
    :return:
    """
    print("正在下載", filename)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}

    request = urllib.request.Request(url, headers = headers)

    return urllib.request.urlopen(request).read().decode("utf-8")


def writepage(html, filename):
    """
    將 html 內容寫入
    :param html: 服務器響應的文件內容
    :return:
    """

    print("正在保存", filename)

    # 等同於 open, write, close
    with open(filename, "w") as f:
        f.write(html)

    print("-" * 30)

def tibacrawler(url, beginpage, endpage):
    """
    :param url: tiba 前段 url
    :param beginpage: 起始頁面
    :param endpage: 結束頁面
    :return:
    """

    for page in range(beginpage, endpage + 1):

        pn = (page - 1)*50
        filename = "No_" + str(page) + ".html"
        fullurl = url + "&pn=" + str(pn)
        print(fullurl)
        html = loadpage(fullurl, filename)
        # print(html)
        writepage(html, filename)


if __name__ == "__main__":
    kw = input("請輸入需要爬取的名稱:")
    beginpage = int(input("請輸入起始頁:"))
    endpage = int(input("請輸入結束頁:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    tibacrawler(fullurl, beginpage, endpage)
