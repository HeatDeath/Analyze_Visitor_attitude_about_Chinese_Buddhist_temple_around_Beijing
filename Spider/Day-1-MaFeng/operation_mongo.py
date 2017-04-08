#coding=utf-8
import pymongo
from selenium import webdriver
import requests
import re

# client = pymongo.MongoClient('localhost', 27017)
# TempleSpider = client['TempleSpider']
# #TempleSpider.drop_collection('temple_detail')
# temple_detail = TempleSpider['temple_detail']
#
# driver = webdriver.PhantomJS()
#
# url = 'http://www.mafengwo.cn/poi/6910.html'
#
# driver.get(url)

#div.m-pagination





#-----------------关于pymongo操作mongodb的一些基本尝试-------------
#---------------------------------------------------------------
# for temple in temple_detail.find():
#     #过滤掉不是汉传佛寺以及不是寺院的景点
#     if '牛街' in temple['temple_name'] or not temple['temple_name'].endswith('寺'):
#         temple_detail.delete_one({'temple_name': temple['temple_name']})
#
# print(temple_detail.find_one({'temple_name': '潭柘寺'}))
#
#
# # $set用来指定一个键并更新键值，若键不存在并创建。
# temple_detail.update({'temple_name': '潭柘寺'}, {"$set": {"TEL": "666666", "Password": "123"}})
#
# print(temple_detail.find_one({'temple_name': '潭柘寺'}))
#
# # 使用修改器$unset时，不论对目标键使用1、0、-1或者具体的字符串等都是可以删除该目标键。
# temple_detail.update({'temple_name': '潭柘寺'}, {"$unset": {"TEL": "", "Password": ""}})
#
# print(temple_detail.find_one({'temple_name': '潭柘寺'}))
#---------------------------------------------------------------

