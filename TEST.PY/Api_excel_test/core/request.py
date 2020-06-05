# D:/python/TEST.PY
# -*- coding:UTF-8 -*-
#基础包：接口测试的封装

import requests
import core.log as log
import json

logging = log.get_logger()

def change_type(value):
    #对dict类型进行中文识别
    #value 传的数据值
    #return 转码后的值
    try:
        if isinstance(eval(value),str):
            return value
        if isinstance(eval(value),dict):
            result = eval(json.dumps(value))
            return result
    except Exception,e:
        logging.error('类型问题 %s',e)

def api(method,url,data,headers):
    #自定义一个接口测试的方法
    #method：请求类型  url：地址 data：数据  headers：请求头  return：code码
    global results
    try:
        if method == ('post' or 'POST'):
            results = requests.post(url,data,headers=headers)
        if method == ('get' or 'GET'):
            results = requests.get(url,data,headers=headers)
        if method == ('put' or 'PUT'):
            results = requests.put(url,data,headers=headers)
        if method == ('delete' or 'DELETE'):
            results = requests.delete(url,headers=headers)
        if method == ('patch' or 'PATCH'):
            results =requests.patch(url,data,headers=headers)
        if method == ('options' or 'OPTIONS'):
            results = requests.options(url,headers=headers)
        response = results.json()
        code = response.get('code')
        return code
    except Exception,e:
        logging.error('service is error',e)

def content(method,url,data,headers):
    #请求response可用自定义检查结果 method-请求类型 url-地址 data-请求参数 headers-请求headers message-信息
    global results
    try:
        if method == ('post' or 'POST'):
            results = requests.post(url,data,headers=headers)
        if method == ('get' or 'GET'):
            results = requests.get(url,data,headers=headers)
        if method == ('put'or 'PUT'):
            results = requests.put(url,data,headers=headers)
        if method == ('patch' or 'PATCH'):
            results = requests.patch(url,data,headers=headers)
        response = results.json()
        message = response.get('message')
        result = response.get('result')
        content = {'message':message,'result':result}
        return content
    except Exception,e:
        logging.error('请求失败 %s' % e)


