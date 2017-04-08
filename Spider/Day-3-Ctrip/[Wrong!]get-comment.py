#coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import re
import random
from selenium import webdriver
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

def get_comment_and_insert(temple_name, bsObj):
    comment_list = bsObj.find_all("span", class_="heightbox")
    for comment in comment_list:
        # data = {
        #     'temple_name': temple_name,
        #     'temple_comment': comment.get_text(),
        #     'data_source': '携程'
        # }
        # temple_comment_Ctrip.insert_one(data)

        print(temple_name+comment.get_text())

# # 只有一页评论的寺院
# temple_url ="http://you.ctrip.com/sight/beijing1/1415329.html"

def get_page_source(temple):
    temple_name = temple['temple_name']
    temple_url = temple['temple_url']
    # 有多页评论的寺院
    #temple_url = "http://you.ctrip.com/sight/Beijing1/5161.html"

    search_response = requests.get(temple_url, get_user_agent())

    bsObj = BeautifulSoup(search_response.text, 'lxml')

    get_comment_and_insert(temple_name, bsObj)
    # print(type(bsObj.find("div", class_="ttd_pager cf")))

    #判断是否需要翻页
    if bsObj.find("div", class_="ttd_pager cf") != None:
        for i in range(int(bsObj.find("b", class_="numpage").get_text())-1):
            driver.find_element_by_css_selector('a[class="nextpage"]').click()

            time.sleep(random.randrange(8))

            bsObj = BeautifulSoup(driver.page_source, 'lxml')
            get_comment_and_insert(temple_name, bsObj)
    else:
        print("just one page!")

if __name__ == "__main__":
    # client = pymongo.MongoClient('localhost', 27017)
    # TempleSpider = client['TempleSpider']
    # temple_url_Ctrip = TempleSpider['temple_url_Ctrip']
    # temple_comment_Ctrip = TempleSpider['temple_comment_Ctrip']

    driver = webdriver.PhantomJS()

    # for temple in temple_url_Ctrip.find()[:1]:
    #     get_page_source(temple)

    temple = {
        'temple_name': 'aaa',
        'temple_url': "http://you.ctrip.com/sight/Beijing1/5161.html"
    }
    get_page_source(temple)

    # <span class="heightbox"> 盛放评论的容器
    # <b class="numpage">18</b> 盛放页数的容器
    # div class="ttd_pager cf" 放页码翻页的容器

    # ---------------------------------
    # 测试只有一页评论的寺院
    # temple = {
    #     'temple_name': 'aaa',
    #     'temple_url': 'http://you.ctrip.com/sight/beijing1/1415329.html'
    # }
    # ---------------------------------


