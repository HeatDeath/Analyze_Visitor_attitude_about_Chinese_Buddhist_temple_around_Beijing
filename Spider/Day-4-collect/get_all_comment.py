#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']

temple_comment = TempleSpider['temple_comment']
temple_comment_Dianping = TempleSpider['temple_comment_Dianping']
temple_comment_Ctrip = TempleSpider['temple_comment_Ctrip']

# 用于储存所有评论信息的 collection
temple_comment_collect = TempleSpider['temple_comment_collect']


for temple in temple_comment.find():
    data = {
        'temple_name': temple['temple_name'],
        'temple_comment': temple['temple_comment'],
        'data_source': '蚂蜂窝'
    }
    temple_comment_collect.insert_one(data)
    print(temple)

for temple in temple_comment_Dianping.find():
    data = {
        'temple_name': temple['temple_name'],
        'temple_comment': temple['temple_comment'],
        'data_source': temple['data_source']
    }
    temple_comment_collect.insert_one(data)
    print(temple)


for temple in temple_comment_Ctrip.find():
    data = {
        'temple_name': temple['temple_name'],
        'temple_comment': temple['temple_comment'],
        'data_source': temple['data_source']
    }
    temple_comment_collect.insert_one(data)
    print(temple)


