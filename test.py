# coding:utf-8

# from interface_qa import remove_needless_sentences, sentnce_segmentation
#
# text = "我国使用的手机号码为11"
#
# a = sentnce_segmentation(text)
# print(a)
#
# # b = remove_needless_sentences(a)
# # print(b)

import requests

response = requests.get("http://127.0.0.1:5000/qaByBd/头像是什么")
print(response.text)