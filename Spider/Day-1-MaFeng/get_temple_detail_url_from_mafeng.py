#coding=utf-8
from bs4 import BeautifulSoup
import pymongo
import requests
from urllib import parse
import pprint
import random

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

def get_temple_detail_url(search_key_word):

    temple_detail = TempleSpider['temple_detail']

    #http://www.mafengwo.cn/search/s.php?q=%E6%BD%AD%E6%9F%98%E5%AF%BA

    search_url = 'http://www.mafengwo.cn/search/s.php?q={}'.format(parse.quote(search_key_word, encoding='utf-8'))

    #search_url = 'http://www.mafengwo.cn/search/s.php?q={}'.format(search_key_word)
    #print(search_url)

    headers = {"user-agent": random.choice(user_agent_list)}
    search_response = requests.get(search_url, headers)
    search_response.encoding = 'utf-8'

    bsObj = BeautifulSoup(search_response.text, 'lxml')

    #print(bsObj)
    try:
        for i in bsObj.select_one('div[data-category="poi"]').find_all("div", class_="clearfix"):
            if '景点' in i.find("h3").get_text() and '北京' in i.find_all("li")[0].find("a").get_text():
                temple_detail_url = i.find("h3").find("a").get("href")
                data = {
                    'temple_name': search_key_word,
                    'temple_url': temple_detail_url
                }

                print(data)
                temple_detail.insert_one(data)
                pass
    except:
        pass

if __name__ == "__main__":

    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_name_table = TempleSpider['temple_name_table']

    for temple in temple_name_table.find():
        if int(temple['temple_comment_num']) >= 10:
            search_key_word = temple['temple_name']
            get_temple_detail_url(search_key_word)
    #pprint.pprint(temple_name_table.find_one())

    #get_temple_detail_url('潭柘寺')





'''
#data-category="poi"
path = "get_temple_detail_url_from_mafeng_test.html"

def get_temple_detail_url(path):
    with open(path, 'rb') as page_html_source:
        bsObj = BeautifulSoup(page_html_source, 'lxml')
        #per_page_len = len(bsObj.find("div",data-category="poi")
        #per_page_len = len(bsObj.select_one('div[data-category="poi"]').find_all("div", class_="clearfix"))
        #print(per_page_len)
        for i in bsObj.select_one('div[data-category="poi"]').find_all("div", class_="clearfix"):
            if '景点' in i.find("h3").get_text() and '北京' in i.find_all("li")[0].find("a").get_text():
                print(i.find("h3").find("a").get("href"))
get_temple_detail_url(path)
'''