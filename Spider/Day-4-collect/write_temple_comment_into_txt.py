#coding=utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']
temple_comment_collect = TempleSpider['temple_comment_collect']

temple_name_list = ['碧云寺', '广化寺', '万寿寺', '卧佛寺', '大觉寺', '白塔寺', '圣泉寺',
                    '五塔寺', '云居寺', '法海寺', '戒台寺', '智化寺', '法源寺', '潭柘寺',
                    '红螺寺', '广济寺', '龙泉寺']

#temple_name = "碧云寺"
for temple_name in temple_name_list[1:]:
    with open('{}_comment.txt'.format(temple_name), 'a', encoding='utf-8', errors='ignore') as txt_file:
        for temple in temple_comment_collect.find():
            if temple['temple_name'] == temple_name:
                txt_file.write(temple['temple_comment'])




# --------------------------------------------
# 获取已经抓取的寺院的名称 list
# temple_name_list = []
# for temple in temple_comment_collect.find():
#     temple_name_list.append(temple['temple_name'])
#
# temple_name_list_no_repeat = list(set(temple_name_list))
#
# print(temple_name_list_no_repeat)
# print(len(temple_name_list_no_repeat))
# --------------------------------------------

