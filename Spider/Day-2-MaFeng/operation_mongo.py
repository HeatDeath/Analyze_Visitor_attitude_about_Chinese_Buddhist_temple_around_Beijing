#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']

#temple_detail = TempleSpider['temple_detail']

temple_comment = TempleSpider['temple_comment']




# ---------------------------------------------
# 抓取大觉寺时发生错误，清除，重新抓取
# for temple in temple_comment.find():
#     # 过滤掉不是汉传佛寺以及不是寺院的景点
#     if temple['temple_name'] == '大觉寺':
#         temple_comment.delete_one({'temple_name': temple['temple_name']})
# ---------------------------------------------

# ---------------------------------------------
# 清除卧佛寺及之前的的寺院信息, 圣泉寺
# i = 0
# for temple in temple_detail.find():
#     temple_detail.delete_one({'temple_name': temple['temple_name']})
#     i += 1
#     if i == 1:
#         break
# ---------------------------------------------

# ---------------------------------------------
# 到卧佛寺的时候出现错误，差了3条数据，手工录入好了...
# data = {
#     'temple_name': '卧佛寺',
#     'temple_comment': '可以说是植物园里最喜欢的地方了~~ 两旁的水杉都好漂亮，走在栈道上特有感觉，喜欢看着两边的小溪流潺潺流过.不过今年去的不是时候啊，基本上没水了。。。 水杉也都还没长出叶子，还是应该5月份去比较好~反正来植物园一定要到这儿来走一走~ 真的很不错~'
# }
# temple_comment.insert_one(data)
# ---------------------------------------------

# temple_comment = TempleSpider['temple_comment']
# temple_detail_old = TempleSpider['temple_detail_old']

# -------------------------------------
# 发现法海寺的 url 冗余，有2个重复的，所以要修复一下
# i = 0
# for temple in temple_detail.find():
#     if temple['temple_name'] == '法海寺':
#         temple_detail.delete_one({'temple_name': temple['temple_name']})
#         i += 1
#         if i == 2:
#             break
# -------------------------------------

# -------------------------------------
# 把 temple_detail 中的数据复制一份到 temple_detail_old 中
# for temple in temple_detail.find():
#     data = {
#         'temple_name': temple['temple_name'],
#         'temple_url': temple['temple_url']
#     }
#     temple_detail_old.insert_one(data)
# -------------------------------------

# -------------------------------------
# 测试一下我的数据到底在不在
# data = {
#     'temple_name': '大悲寺',
#     'temple_comment': '1024'
# }
# temple_comment.insert_one(data)

# for temple in temple_comment.find():
#     print(temple)
# -------------------------------------

# --------------------------------------
# # 抓取法海寺的时候出现错误，清除，重新抓取
# for temple in temple_comment.find():
#     # 过滤掉不是汉传佛寺以及不是寺院的景点
#     if temple['temple_name'] == '法海寺':
#         temple_comment.delete_one({'temple_name': temple['temple_name']})
# #代码写错了，不小心 拖库 了...mdzz，还得重新抓取一次  :(
# --------------------------------------



# --------------------AT·Field------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# 十分危险的语句，封印...键值可怕，简直...
# -----------------------------------------------------
# --TempleSpider.drop_collection('temple_comment')------
# -----------------------------------------------------


