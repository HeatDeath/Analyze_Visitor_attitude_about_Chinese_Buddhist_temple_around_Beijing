# coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import re
import random
from selenium import webdriver
import time

def get_comment_and_insert(temple_name, bsObj):
    comment_list = bsObj.select('div[id="sightcommentbox"]')[0].find_all("span", class_="heightbox")
    # print(comment_list)
    # print("---------"+str(len(comment_list))+"-----------------")
    for comment in comment_list:
        data = {
            'temple_name': temple_name,
            'temple_comment': comment.get_text().strip(),
            'data_source': '携程'
        }
        temple_comment_Ctrip.insert_one(data)
        print(temple_name+comment.get_text())

    #time.sleep(random.randrange(10, 20))
    time.sleep(random.randrange(5))


# # 只有一页评论的寺院
# temple_url ="http://you.ctrip.com/sight/beijing1/1415329.html"

def get_page_source(temple):
    temple_name = temple['temple_name']
    temple_url = temple['temple_url']
    # 有多页评论的寺院
    # temple_url = "http://you.ctrip.com/sight/Beijing1/5161.html"

    # 此处设计的逻辑错误
    #search_response = requests.get(temple_url, get_user_agent())
    #print(temple_url)

    driver.get(temple_url)

    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    # print(bsObj)

    get_comment_and_insert(temple_name, bsObj)
    # print(type(bsObj.find("div", class_="ttd_pager cf")))

    # 判断是否需要翻页
    if bsObj.find("div", class_="ttd_pager cf") != None:
        for i in range(int(bsObj.find("b", class_="numpage").get_text())):
            try:
                driver.find_element_by_css_selector('a[class="nextpage"]').click()

                time.sleep(random.randrange(5, 10))

                bsObj = BeautifulSoup(driver.page_source, 'lxml')
                get_comment_and_insert(temple_name, bsObj)

                print("当前浏览第{}页评论".format(i+2))
            except:
                pass
    else:
        print("just one page!")


if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_url_Ctrip = TempleSpider['temple_url_Ctrip']
    temple_comment_Ctrip = TempleSpider['temple_comment_Ctrip']

    driver = webdriver.PhantomJS()

    for temple in temple_url_Ctrip.find()[3:4]:
        get_page_source(temple)
        # time.sleep(random.randrange(50, 80))

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

    # ---------------------------------
    # 测试有多个页评论的寺院
    # temple = {
    #     'temple_name': 'aaa',
    #     'temple_url': "http://you.ctrip.com/sight/Beijing1/5161.html"
    # }
    # get_page_source(temple)


