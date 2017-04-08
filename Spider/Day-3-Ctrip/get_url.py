#coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import re
import random
from selenium import webdriver
from urllib import parse
import time

def get_user_agent():
    user_agent_list = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
            ]
    headers = {"user-agent": random.choice(user_agent_list)}
    return headers

#temple_name = '云居寺'

def get_temple_url_and_insert(temple_name):
    host_url = 'http://you.ctrip.com/searchsite/Sight?query='

    part_url = parse.quote(temple_name+'北京', encoding='utf-8')

    url = host_url + part_url

    search_response = requests.get(url, get_user_agent())

    bsObj = BeautifulSoup(search_response.text, 'lxml')

    #print(bsObj)

    home_url = "http://you.ctrip.com"

    part_temple_url = bsObj.find("ul", class_="jingdian-ul cf").find("a").get("href")

    temple_url = home_url+part_temple_url

    print(temple_url)

    data = {
        'temple_name': temple_name,
        'temple_url': temple_url
    }
    temple_url_Ctrip.insert_one(data)

    time.sleep(random.randrange(5))

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_url_Ctrip = TempleSpider['temple_url_Ctrip']

    temple_name_list = ['法源寺', '云居寺', '广济寺', '潭柘寺', '大觉寺', '戒台寺',
                        '白塔寺', '法海寺', '五塔寺', '碧云寺', '卧佛寺', '红螺寺', '智化寺', '广化寺', '万寿寺']


    for temple_name in temple_name_list:
        get_temple_url_and_insert(temple_name)


    # 打算尝试这个，结果失败了，不知道哪里不太对
    # map(get_temple_url_and_insert, temple_name_list)






'''
关于ctrip检索内容的尝试

In [54]: a=parse.quote('万寿寺北京', encoding='utf-8')

In [55]: a
Out[55]: '%E4%B8%87%E5%AF%BF%E5%AF%BA%E5%8C%97%E4%BA%AC'

In [56]: a.split("%")
Out[56]:
['', 'E4', 'B8', '87', 'E5', 'AF', 'BF', 'E5', 'AF', 'BA', 'E5', '8C', '97', 'E4', 'BA', 'AC']

In [57]: a
Out[57]: '%E4%B8%87%E5%AF%BF%E5%AF%BA%E5%8C%97%E4%BA%AC'

In [58]: type(a.split("%"))
Out[58]: list

In [59]: a.split("%")[1:]
Out[59]:
['E4', 'B8', '87', 'E5', 'AF', 'BF', 'E5', 'AF', 'BA', 'E5', '8C', '97', 'E4', 'BA', 'AC']

In [60]: str=''

In [61]: for i in a.split("%")[1:]:
    ...:     i = '%25'+i
    ...:     str = str + i
    ...:

In [62]: str
Out[62]: '%25E4%25B8%2587%25E5%25AF%25BF%25E5%25AF%25BA%25E5%258C%2597%25E4%25BA%25AC'

'''

# ctrip 居然可以用 requests 请求！！！

#http://piao.qunar.com/ticket/list.htm?keyword=%E4%BA%91%E5%B1%85%E5%AF%BA&city=%E5%8C%97%E4%BA%AC
# keyword = xxx    city = beijing

#http://you.ctrip.com/searchsite/Sight?query=%25e4%25ba%2591%25e5%25b1%2585%25e5%25af%25ba%25e5%258c%2597%25e4%25ba%25ac
# query = xxx北京