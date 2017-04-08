#coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import re
import random
from selenium import webdriver
from urllib import parse
import time

# 用bs4处理评论页源码，并将获取到的数据储存到名为 temple_comment_Dianping 的 collection 中
def get_comment_use_bs4(temple_name, bsObj):
    comment_list = bsObj.find("div", class_="comment-list").find_all("div", class_="J_brief-cont")
    for comment in comment_list:
        data = {
            'temple_name': temple_name,
            'temple_comment': comment.get_text().strip(),
            'data_source': '大众点评'
        }
        temple_comment_Dianping.insert_one(data)
        print(temple_name+comment.get_text().strip())

def get_comment(temple):
    temple_name = temple['temple_name']
    temple_url = temple['temple_url']
    driver.get(temple_url)
    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    # 评论少于一页的右下角没有页码,一页评论有20条评论
    get_comment_use_bs4(temple_name, bsObj)

    # print(comment_list)
    # print(len(comment_list))

    if len(bsObj.find("div", class_="Pages").get_text().strip()) > 0:

        # 需要经过总评论页数-1次翻页
        for i in range(int(bsObj.find_all("div", class_="Pages")[1].find_all("a")[-2].get_text())-1):
            try:
                driver.find_element_by_css_selector('a[title="下一页"]').click()
                time.sleep(5)
                bsObj = BeautifulSoup(driver.page_source, 'lxml')
                get_comment_use_bs4(temple_name, bsObj)
                time.sleep(random.randrange(10, 20))
            except:
                pass

        #print(bsObj.find_all("div", class_="Pages")[1].find_all("a")[-2].get_text())

    else:
        pass

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_url_DianPing = TempleSpider['temple_url_DianPing']
    temple_comment_Dianping = TempleSpider['temple_comment_Dianping']

    driver = webdriver.PhantomJS()

    # for temple in temple_url_DianPing.find()[8:]:
    #     get_comment(temple)

    temple = {
        'temple_name':'五塔寺',
        'temple_url':"http://www.dianping.com/shop/11271012/review_more"
    }

    get_comment(temple)

    # --------------------------------------------
    # 测试只有一页评论或不满一页的评论页面
    # temple = {
    #     'temple_name': '111',
    #     'temple_url': "http://www.dianping.com/shop/50318412/review_more"
    # }
    # get_comment(temple)
    # --------------------------------------------

    # ----------------------------------------------
    # 用于测试本寺院的评论页数
    # temple_url = "http://www.dianping.com/shop/50318412/review_more"
    # driver.get(temple_url)
    # bsObj = BeautifulSoup(driver.page_source, 'lxml')
    # # 评论少于一页的右下角没有页码,一页评论有20条评论
    # comment_list = bsObj.find("div", class_="comment-list").find_all("div", class_="J_brief-cont")
    # print(comment_list)
    # print(len(comment_list))
    #
    # if len(bsObj.find("div", class_="Pages").get_text().strip()) > 0:
    #     print('True')
    # else:
    #     print('False')
    # ----------------------------------------------

