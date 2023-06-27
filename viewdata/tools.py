import pymysql
import requests
import json

def get_conn():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        database="views",
        password="root",
        charset="utf8",
        port=3306
    )

    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res



def bigdata_toplist():
    sql = "select * from basic_info"
    res = query(sql)
    data = []
    for i in res:
        for j in i:
            data.append(j)
    return res

def bigdata_company():
    sql = "SELECT * from package_rank ORDER BY package DESC"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': float(i[1])})
    # print(data)
    return data

def bigdata_chart3():
    sql = "SELECT * from chart3"
    res = query(sql)
    data = []
    for i in res:
        data.append({'name': i[0], 'value': int(i[1])})
    return data

def bigdata_sales_rank():
    sql = "select * from goods_sales_rank"
    res = query(sql)
    data = []
    for i in res:
        data.append(i)
    return data

def bigdata_chart2_data():
    sql = "select * from chart2"
    res = query(sql)
    ydata = []
    xdata = []
    for i in res:
        ydata.append({'name': i[0], 'value': int(i[1])})
        xdata.append(i[0])
    return ydata, xdata

def bigdata_ceshi5_data():
    res1 = query("select name,value from ceshis5 where id=1 ORDER BY value DESC")
    res2 = query("select name,value from ceshis5 where id=2 ORDER BY value DESC")
    res3 = query("select name,value from ceshis5 where id=3 ORDER BY value DESC")
    res4 = query("select name,value from ceshis5 where id=4 ORDER BY value DESC")
    res5 = query("select name,value from ceshis5 where id=5 ORDER BY value DESC")
    res6 = query("select name,value from ceshis5 where id=6 ORDER BY value DESC")
    data1 = {}
    data2 = {}
    data3 = {}
    data4 = {}
    data5 = {}
    data6 = {}
    for i in res1:
        data1[i[0]] = int(i[1])
    for i in res2:
        data2[i[0]] = int(i[1])
    for i in res3:
        data3[i[0]] = int(i[1])
    for i in res4:
        data4[i[0]] = int(i[1])
    for i in res5:
        data5[i[0]] = int(i[1])
    for i in res6:
        data6[i[0]] = int(i[1])
    return data1,data2,data3,data4,data5,data6


def bigdata_chart4_data():
    res = query("SELECT * from bigdata_chart4")
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])
        data4.append(i[3])
    return data1,data2,data3,data4

def bigdata_chart5_data():
    res = query("SELECT * from bigdata_chart5")
    data1 = []
    data2 = []
    for i in res:
        data1.append(i[0])
        data2.append(i[1])
    return data1,data2

if __name__ == '__main__':
    print(index3_chart8_data())