#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']

#temple_detail = TempleSpider['temple_detail']

temple_comment_Dianping = TempleSpider['temple_comment_Dianping']

# 五塔寺冗余，需要重新抓取！

# temple_comment_Dianping.delete_many({'temple_name': '五塔寺'})





# ---------------------------------------
# 将数据来源从 DianPing 修改为 大众点评
# for temple in temple_comment_Dianping.find():
# temple_comment_Dianping.update_many({'temple_name': '法源寺'}, {"$set": {"data_source": "大众点评"}})
# ---------------------------------------





