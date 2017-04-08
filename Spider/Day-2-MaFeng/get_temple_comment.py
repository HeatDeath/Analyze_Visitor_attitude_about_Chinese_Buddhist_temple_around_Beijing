#coding=utf-8
import pymongo
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random

# 使用 selenium+PhantomJS 获取各个评论页的 html 源码
def get_comment_pages(temple_url):
    driver = webdriver.PhantomJS()

    #url = 'http://www.mafengwo.cn/poi/6910.html'
    url = temple_url

    driver.get(url)

    # 尝试获取评论页的数量，没有就算了...
    try:
        comment_pages_count = driver.find_element_by_css_selector('div.m-pagination>span.count>span').text
    except:
        pass
    #print(comment_pages_count)

    # comment_pages = []
    # comment_pages.append(driver.page_source)

    get_comment(temple_name, driver.page_source)

    # 当评价数量大于 15 ，即当前寺院的评论数量大于 1 页的时候，模拟翻页
    if get_comment_count(driver.page_source):
        # 模拟浏览器翻页过程
        for i in range(int(comment_pages_count)-1):
        #for i in range(3):
            try:
                # 翻页
                driver.find_element_by_css_selector('a[class="pi pg-next"]').click()

                # 将该页面的评论依次插入到名为 temple_comment 的 collection 中
                get_comment(temple_name, driver.page_source)

                # spider随机睡眠时间
                time.sleep(random.randrange(10, 20))

                # comment_pages.append(driver.page_source)
                #
                # print(comment_pages)
                # #print(len(comment_pages))
                # #print(driver.page_source)
                # return comment_pages

            except:
                print(temple_url)
                print('第{}页时发生错误'.format(i+1))
                pass
    else:
        pass



# 获取评论详情文本
def get_comment(temple_name, comment_page):
    bsObj = BeautifulSoup(comment_page, 'lxml')
    comment_list = bsObj.select('div[data-cs-p="评论列表"]')[0].find_all("p", class_="rev-txt")
    #print(comment_list)

    # 将获取到的数据插入到名为 temple_comment 的 collection 中
    for comment in comment_list:
        data = {
            'temple_name': temple_name,
            'temple_comment': comment.get_text(),
            'data_source': '蚂蜂窝'
        }
        print(temple_name+comment.get_text())
        temple_comment.insert_one(data)

def get_comment_count(driver_page_source):
    bsObj = BeautifulSoup(driver_page_source, 'lxml')
    comment_count = bsObj.select('div[data-cs-p="评论列表"]')[0].find("em").get_text()
    print(int(comment_count))
    if int(comment_count) > 15:
        return True
    else:
        return False

# for comment_page in comment_pages:
#     get_comment(comment_page)
#list(map(get_comment, comment_pages))

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_detail = TempleSpider['temple_detail']
    temple_comment = TempleSpider['temple_comment']

    for temple in temple_detail.find():
        temple_name = temple['temple_name']
        temple_url = temple['temple_url']
    # temple_name = '潭柘寺'
    # temple_url = 'http://www.mafengwo.cn/poi/6910.html'
    #     for comment_page in get_comment_pages(temple_url):
    #         get_comment(temple_name, comment_page)
        get_comment_pages(temple_url)

    # temple_name = '圣泉寺'
    # temple_url = 'http://www.mafengwo.cn/poi/6794937.html'
    # get_comment_pages(temple_url)