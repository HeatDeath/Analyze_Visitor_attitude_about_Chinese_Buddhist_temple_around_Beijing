#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']

#temple_detail = TempleSpider['temple_detail']

temple_comment_Ctrip = TempleSpider['temple_comment_Ctrip']

# temple_comment_Ctrip.delete_many({'temple_name': '潭柘寺'})






