# coding:utf-8
from flask import Flask
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import pymysql
import random
from fake_useragent import UserAgent
import time
from multiprocessing import Pool
ua=UserAgent()
print(ua.random)


db = pymysql.connect("localhost", "root", "root", "qa",charset='utf8')

cursor = db.cursor()
sql = "select question from qa_old"
cursor.execute(sql)
questions = cursor.fetchall()
def download(question):
    url = "http://wechat.riskeys.com/ws_server/answer"
    payload = "{\"questionId\":2,\"answer\":\"%s\"}" % question
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
    }
    try:
        response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
        response.encoding = response.apparent_encoding

        data = json.loads(response.text)
    except Exception as e:
        print(e)
        pass


    print(data)
    try:
        answer = data['data_info']['messageList'][0]['value']
        print(question)
        print(answer)
        cursor = db.cursor()
        sql = "INSERT INTO qa (question, answer) VALUES (%s, %s)"
        try:
            if question[0] is not None and len(question[0].replace('\r', '').replace('\n', '').strip()) > 0:
                cursor.execute(sql, (question[0].encode('utf-8'), answer.encode('utf-8')))
                db.commit()
                time.sleep(random.uniform(0, 3))
            else:
                pass
        except Exception as e:
            print(e)
            pass
    except Exception as e:
        print(e)
        pass


if __name__=='__main__':
    print("数据开始进行下载，请等待。。。。")
    start=time.time()
    pool=Pool(10)
    pool.map(download,questions)
    pool.close()
    pool.join()

    end=time.time()
    print("下载完毕，用时:%s"%(end-start))
    print('数据下载完成，请验收。。。')






