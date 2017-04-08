#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']
temple_detail = TempleSpider['temple_detail_old']

temple_name_list =[]
for temple in temple_detail.find():
    temple_name_list.append(temple['temple_name'])

temple_name_list_no_repeat = list(set(temple_name_list))

print(temple_name_list_no_repeat)
print(len(temple_name_list_no_repeat))

#['法源寺', '云居寺', '广济寺', '潭柘寺', '大觉寺', '戒台寺', '白塔寺', '法海寺', '五塔寺',
# '万寿寺', '碧云寺', '卧佛寺', '红螺寺', '智化寺', '广化寺', '圣泉寺']
# 删除圣泉寺， 万寿寺手动添加
# 添加龙泉寺

temple_name_list_no_repeat = ['法源寺', '云居寺', '广济寺', '潭柘寺', '大觉寺', '戒台寺',
                              '白塔寺', '法海寺', '五塔寺', '碧云寺', '卧佛寺',
                              '红螺寺', '智化寺', '广化寺', '龙泉寺']