#coding=utf-8
import pymongo
from selenium import webdriver
import time
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
TempleSpider = client['TempleSpider']
temple_detail = TempleSpider['temple_detail']

driver = webdriver.PhantomJS()

url = 'http://www.mafengwo.cn/poi/6910.html'

driver.get(url)

#div.m-pagination

commit_pages_count = driver.find_element_by_css_selector('div.m-pagination>span.count>span').text

#print(commit_pages_count)

for i in range(int(commit_pages_count)-1):
    driver.find_element_by_css_selector('div[class="pi pg-next"]').click()
    time.sleep(1)
    driver.page_source
    ##pagelet-block-3f3b74c86fb72da3a282c12012b9dece > div
    # data-cs-p="评论列表"