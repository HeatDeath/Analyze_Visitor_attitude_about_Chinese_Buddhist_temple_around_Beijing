#coding=utf-8
import pymongo
import MySQLdb

#--------------------------数据库启动函数------------------------------
def start_MySQL():
    conn = MySQLdb.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='roottest',
            db ='temple_comment_table',
            charset='gbk')
    cur = conn.cursor()
    myConn_list = [conn, cur]
    return myConn_list
#---------------------------------------------------------------------

#--------------------------关闭数据库--------------------------------
def close_MySQL(cur,conn):
    cur.close()
    conn.commit()
    conn.close()
#------------------------------------------------------------------

if __name__ == "__main__":
    client = pymongo.MongoClient('localhost', 27017)
    TempleSpider = client['TempleSpider']
    temple_comment_collect = TempleSpider['temple_comment_collect']

    myConn_list = start_MySQL()
    cur = myConn_list[1]
    conn = myConn_list[0]

    sqli = "insert into temple_comment values(%s,%s,%s)"

    for temple in temple_comment_collect.find():
        try:
            cur.execute(sqli, (temple['data_source'],
                               temple['temple_name'],
                               temple['temple_comment']))

            print(temple)
        except:
            pass



        # cur.execute(sqli, (temple['data_source'],
        #                    temple['temple_name'],
        #                    temple['temple_comment']))
        # print(temple)

    close_MySQL(cur, conn)

