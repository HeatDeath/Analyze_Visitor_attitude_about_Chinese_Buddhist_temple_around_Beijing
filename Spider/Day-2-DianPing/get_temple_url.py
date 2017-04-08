#coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import re
import random
from selenium import webdriver
from urllib import parse
import time

def get_temple_url(driver, temple_name):
    host_url = 'http://www.dianping.com/search/keyword/2/0_'

    #temple_name = '云居寺'

    part_url = parse.quote(temple_name+'景点', encoding='utf-8')

    url = host_url + part_url

    driver.get(url)

    bsObj = BeautifulSoup(driver.page_source, 'lxml')

    temple_code = re.findall(r"[0-9]*$", bsObj.select('a[data-hippo-type="shop"]')[0].get("href"))[0]

    #print(temple_code)

    temple_url = "http://www.dianping.com/shop/{}/review_more".format(temple_code)

    data = {
        'temple_name': temple_name,
        'temple_code': temple_code,
        'temple_url': temple_url
    }

    print(temple_url)

    temple_url_DianPing.insert_one(data)

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_url_DianPing = TempleSpider['temple_url_DianPing']

    driver = webdriver.PhantomJS()

    # temple_list = ['法源寺', '云居寺', '广济寺', '潭柘寺', '大觉寺', '戒台寺',
    #                '白塔寺', '法海寺', '五塔寺', '碧云寺', '卧佛寺',
    #                '红螺寺', '智化寺', '广化寺', '龙泉寺']

    temple_list = ['五塔寺', '碧云寺', '卧佛寺', '红螺寺', '智化寺', '广化寺', '龙泉寺']
    for temple_name in temple_list:
        get_temple_url(driver, temple_name)
        time.sleep(random.randrange(10, 20))


# --------------------------------------------------------------------
# 大众点评反爬虫的措施似乎很麻烦，遂放弃requests
# selenium+PhantomJS虽然慢了点，但是百试百灵...
# user_agent_list = [
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#             "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#             "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#             "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
#         ]
#
# headers = {"user-agent": random.choice(user_agent_list)}
# search_response = requests.get(url+temple_name+'景点', headers)
# bsObj = BeautifulSoup(search_response.text, 'lxml')
# print(bsObj)

# temple_code = bsObj.find("div", class_="tit")
# #temple_code = re.findall(r"[0-9]*$", bsObj.find("div.tit").find("a").get("href"))[0]
# print(temple_code)
# --------------------------------------------------------------------

