#coding=utf-8
from selenium import webdriver
import time

def get_temple_page_source():

    driver = webdriver.PhantomJS()

    url = 'http://www.mafengwo.cn/mdd/map/10065.html'

    driver.get(url)

    time.sleep(1)

    driver.find_element_by_css_selector('a[data-channel="search"]').click()
    time.sleep(1)


    driver.find_element_by_css_selector('div.input_wrapper>input').clear()
    driver.find_element_by_css_selector('div.input_wrapper>input').send_keys('寺')
    time.sleep(1)


    driver.find_element_by_css_selector('div.input_wrapper>span').click()

    time.sleep(3)

    #reponse_html_page = driver.page_source

    #style="overflow: auto; height: 576px;"

    #reponse_html_page = driver.find_element_by_css_selector('div.list>ul').text

    # print(type(reponse_html_page))
    #print(driver.page_source)

    pageSource_list = []

    pageSource_list.append(driver.page_source)

    for i in range(4):
        driver.find_element_by_css_selector('div.m-pagination>a.pg-next').click()
        time.sleep(3)
        #print(driver.page_source)
        pageSource_list.append(driver.page_source)

    return pageSource_list


if __name__ == "__main__":
    get_temple_page_source()