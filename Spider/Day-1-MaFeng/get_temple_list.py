from bs4 import BeautifulSoup
import pymongo
from .get_temple_page_source import get_temple_page_source
from multiprocessing import Pool

def get_temple_name_from_per_page_source(page_html_source):
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_name_table = TempleSpider['temple_name_table']

    bsObj = BeautifulSoup(page_html_source, 'lxml')
    temple = {}
    for temple_li in bsObj.find_all("ul")[1].find_all("li"):
        temple['temple_name'] = temple_li.find("h3").get_text()
        temple['temple_comment_num'] = temple_li.find("div", class_="comments_num comments_num2").find_all("span")[0].get_text()
        temple['temple_tourist_num'] = temple_li.find("div", class_="comments_num comments_num2").find_all("span")[1].get_text()
        print(temple)
        data = {
            'temple_name': temple['temple_name'].strip(),
            'temple_comment_num': temple['temple_comment_num'],
            'temple_tourist_num': temple['temple_tourist_num']
        }
        temple_name_table.insert_one(data)

if __name__ == "__main__":

    pool = Pool()
    pool.map(get_temple_name_from_per_page_source, get_temple_page_source())



'''
path = "get_temple_list_test.html"

def get_temple_name_from_per_page_source(path):
    with open(path, 'rb') as page_html_source:
        bsObj = BeautifulSoup(page_html_source, 'lxml')
        per_page_len = len(bsObj.find_all("h3"))
        #temple_message_from_mafengwo = []
        #for i in range(per_page_len):
        #print(per_page_len)
        temple = {}
        for temple_li in bsObj.find_all("ul")[1].find_all("li"):
            temple['temple_name'] = temple_li.find("h3").get_text()
            temple['temple_comment_num'] = temple_li.find("div", class_="comments_num comments_num2").find_all("span")[0].get_text()
            temple['temple_tourist_num'] = temple_li.find("div", class_="comments_num comments_num2").find_all("span")[1].get_text()
            print(temple)
            data = {
                'temple_name': temple['temple_name'],
                'temple_comment_num': temple['temple_comment_num'],
                'temple_tourist_num': temple['temple_tourist_num']
            }
            temple_name_table.insert_one(data)
get_temple_name_from_per_page_source(path)
'''

