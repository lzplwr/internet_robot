# coding:utf-8
import requests
from lxml import etree
import json
import urllib.parse
import jieba




def queryByBaidu(question):
    url = "https://wapiknow.baidu.com/index"

    querystring = {"rn": "10", "word": "什么是共保", "lm": "0", "ssid": "0", "from": "0", "bd_page_type": "1",
                   "uid": "B9BFFD2DB0932FDC17AF1039038A5AE7", "pu": "sz@224_240,os@", "init": "middle", "step": "1",
                   "cifr": "p_idx"}

    headers = {
        'pragma': "no-cache",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/65.0.3325.181 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "http://wapiknow.baidu.com/",
        'cookie': "BAIDUID=B9BFFD2DB0932FDC17AF1039038A5AE7:FG=1; BIDUPSID=B9BFFD2DB0932FDC17AF1039038A5AE7; "
                  "PSTM=1520574165; "
                  "BDUSS=dhOXYxMFNkeXloVEhUeWR6Z1JNbGJ"
                  "-Wk9jLWhiV1pwflltZ1FKZmNOTFJLOUJhQVFBQUFBJCQAAAAAAAAAAAEAAAA6pGNEuMrV4WhlYXZlbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGeqFrRnqhaej; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=7; H_PS_PSSID=1465_21119_20883_22074; Hm_lvt_16bc67e4f6394c05d03992ea0a0e9123=1522461790; Hm_lpvt_16bc67e4f6394c05d03992ea0a0e9123=1522463104",
        'connection': "keep-alive",
        'cache-control': "no-cache",
    }

    next_headers = {
        'pragma': "no-cache",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) "
                      "Version/6.0 Mobile/10A5376e Safari/8536.25",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'cache-control': "no-cache",
        'cookie': "BAIDUID=B9BFFD2DB0932FDC17AF1039038A5AE7:FG=1; BIDUPSID=B9BFFD2DB0932FDC17AF1039038A5AE7; PSTM=1520574165; BDUSS=dhOXYxMFNkeXloVEhUeWR6Z1JNbGJ-Wk9jLWhiV1pwflltZ1FKZmNOTFJLOUJhQVFBQUFBJCQAAAAAAAAAAAEAAAA6pGNEuMrV4WhlYXZlbgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANGeqFrRnqhaej; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=7; H_PS_PSSID=1465_21119_20883_22074; BKWPF=3",
        'connection': "keep-alive",
        'postman-token': "5c97e333-fa44-4dd9-840f-bd3bc7886f2d"
    }
    base_url='https://wapiknow.baidu.com'
    querystring['word'] = question
    response = requests.request("GET",url=url, headers=headers, params=querystring)
    html = etree.HTML(response.text.encode('utf-8'))
    detail_urls = html.xpath('//div[@class="slist"]/p/a/@href')[:3]
    titles = html.xpath('//div[@class="slist"]/p/a/text()')[:3]
    answer = {}
    for data in zip(titles, detail_urls):
        if data[0].__contains__('百度百科'):
            # next_url=urllib.parse.unquote(base_url+data[1])
            # next_url=next_url.split('next=')[1]
            # print(next_url)
            #
            #
            # baike_response = requests.get(url=next_url, headers=headers)
            # print(baike_response.content.decode('utf-8').encode('UTF-8'))
            # result=etree.HTML(baike_response.text.encode('UTF-8'))
            # content = result.xpath('/html/head/meta[2]/@content')
            # print(''.join(content))
            # answer['code'] = 200
            # answer['message'] = '解析成功'
            # answer['data'] = content
            # print(json.dumps(answer))
            kw=data[0].split('_')[0]
            url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi"
            querystring = {"scope": "103", "format": "json", "appid": "379020", "bk_key": kw, "bk_length": "600"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            answer['code'] = 200
            answer['message'] = '解析成功'
            answer['data'] = json.loads(response.text)['abstract']
            print(json.dumps(answer))
            return json.dumps(answer)
        else:
            question=data[0]
            next_url=base_url+data[1]
            print(next_url)
            baike_response = requests.get(url=next_url, headers=headers)
            baike_response.encoding = baike_response.apparent_encoding
            result=etree.HTML(baike_response.text)
            content = result.xpath('//div[@class="full-content"]/text()')
            print(''.join(content))
            answer['code'] = 200
            answer['message'] = '解析成功'
            answer['data'] = content
            return json.dumps(answer)



result = queryByBaidu('雇主责任险保障哪些内容')
print(result)
