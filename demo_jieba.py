import requests

url = "https://zhidao.baidu.com/question/256645666.html"

querystring = {"si":"2","qbpn":"1_2","tx":"wiki","wtp":"wk","word":"什么是企业财产险","fr":"solved","from":"","ssid":"0","uid":"B9BFFD2DB0932FDC17AF1039038A5AE7","pu":"sz@224_240,os@","step":"4","bd_page_type":"1","init":"middle"}

headers = {
    'pragma': "no-cache",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://zhidao.baidu.com/index/?fr=new_search_top&word=%E4%BB%80%E4%B9%88%E6%98%AF%E4%BC%81%E4%B8%9A%E8%B4%A2%E4%BA%A7%E9%99%A9&ssid=0&uid=B9BFFD2DB0932FDC17AF1039038A5AE7&step=3",
    'cookie': "BAIDUID=B9BFFD2DB0932FDC17AF1039038A5AE7:FG=1; BIDUPSID=B9BFFD2DB0932FDC17AF1039038A5AE7; PSTM=1520574165; BDUSS=dhOXYxMFNkeXloVEhUeWR6Z1JNbGJ-Wk9jLWhiV1pwflltZ1FKZmNOTFJLOUJhQVFBQUFBJCQAAAAAAAAAAAEAAAA6pGNEuMrV4WhlYXZlbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGeqFrRnqhaej; IKUT=9524; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=7; H_PS_PSSID=1465_21119_20883_22074; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1522135855,1522136183,1522396455,1522460590; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522476173; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522476213; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1522479336",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'postman-token': "b54f6105-8b10-3203-9a84-ee3a08a37447"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.encoding,response.apparent_encoding)
response.encoding = response.apparent_encoding

print(response.text)