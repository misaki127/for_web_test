# D:/python/TEST.PY
# -*- coding:UTF-8 -*-
#数据准备调用mysql

import pymysql.cursors
import logging
import uuid
import time
import common as c

DB = None

def connect(host,user,password,db,port,charset='utf-8'):
    #链接MySQL
    global DB
    if DB == None:
        DB = pymysql.connect(host=host,user=user,password=password,db=db,port=port,charset=charset,cursorclass=pymysql.cursors.DictCursor)
    return DB

def execute(sql):
    #执行SQL
    global DB
    try:
        with DB.cursor() as cursor:
            res = cursor.execute(sql)
            DB.commit()#链接不会默认提交，需要手动提交
        return res
    except Exception,e:
        DB.rollback() #若错误就回滚
        logging.info('sql is empty or error %s',e)

def getNewId(sql):
    #执行SQL获取自增ID
    global DB
    try:
        with DB.cursor() as cursor:
            cursor.execute(sql)
        DB.commit()
        res = cursor.lastrowid
        #获取最新的语句的自增ID
        return res
    except Exception,e:
        DB.rollback() #错误就回滚
        logging.info('sql is empty or error %s',e)

def select(sql):
    #查询语句获取查询结果
    global DB
    try:
        with DB.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            print result
    except Exception,e:
        logging.info('sql is empty or error %s',e)

def setUid():
    #生成一个唯一的Uid
    uid = str(uuid.uuid1())
    id = ''.join(uid.split('-'))
    return id

def setPhone():
    #生成一个唯一的手机号码
    number = time.time()
    phone = int(number * 10)
    return phone

def setEmail():
    #生成一个唯一的邮箱号码
    number = str(int(time.time()))
    email = number[-5:] + c.EMAIL
    return email

def close():
    #关闭MySQL链接
    global DB
    DB.close()