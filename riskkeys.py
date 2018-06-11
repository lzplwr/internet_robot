import requests

url = "http://wechat.riskeys.com/ws_server/answer"

payload = "{\"questionId\":2,\"answer\":\"如何给自己买保险\"}"
headers = {
    'connection': "keep-alive",
    'accept-encoding': "gzip, deflate",
    'content-type': "application/json;charset=UTF-8",
    'unionid': "oeDaQxGWMb3iSHKSRvvC6RlMK89Y",
    'source': "anyi",
    'origin': "http://wechat.riskeys.com",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN",
    'host': "wechat.riskeys.com",
    'referer': "http://wechat.riskeys.com/wxApp.html?from=groupmessage&isappinstalled=0",
    'accept-language': "zh-cn",
    'accept': "application/json, text/plain, */*",
    'content-length': "52",
    'cache-control': "no-cache",
    'postman-token': "7d61f256-8cac-ea49-1c5e-647d421a269a"
    }

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

print(response.text)