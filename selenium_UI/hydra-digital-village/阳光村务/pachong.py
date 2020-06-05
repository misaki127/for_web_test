#encoding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import selenium
import json
import time
import io

end_list = []
url_start = 'https://www.lagou.com/jobs/list_人事?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput='
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
data = {"first":"true","pn":"1","kd":"人事"}


def mian(url_start,url,headers,end_list,data):
    s = requests.sessions
    s = requests.get(url_start,headers=headers)
    cookies = s.cookies
    r = requests.post(url,data=data,headers=headers,cookies=cookies)

    json1 = json.loads(r.text)

    dic1 = json1["content"]["positionResult"]["result"]

    image_url = '//www.lgstatic.com/thumbnail_120x120/'
    for i in dic1:
        dic2={}
        dic2["职位名称"]=i["positionName"]
        dic2["公司名称"]=i["companyFullName"]
        dic2["公司简称"]=i["companyShortName"]
        dic2["公司logo"]=image_url + i["companyLogo"]
        dic2["公司规模"]=i['companySize']
        dic2["公司领域"]=i['industryField']
        dic2["是否上市"]=i['financeStage']
        dic2["公司福利"] = i['companyLabelList']
        dic2["技能要求"] = i['skillLables']
        if i['businessZones'] == None:
            if i['district'] == None:
                dic2["地址"] = i["city"]
            else:
                dic2["地址"] = i["city"] + i["district"]
        else:
            dic2["地址"] = i["city"] + i["district"] + i["businessZones"][0]
        dic2["薪资"]=i['salary']
        dic2['工作年限']=i['workYear']
        dic2['是否全职']=i['jobNature']
        dic2['学历要求']=i['education']
        dic2['企业优势']=i['positionAdvantage']
        dic2['发布时间']=i['createTime'] +' ' + i['formatCreateTime']
        end_list.append(dic2)
    return end_list


file = 'D:/qiuzhi.txt'

for i in range(3):
    data = {"first": "true", "pn": i, "kd": "人事"}
    end_list = mian(url_start, url, headers, end_list, data)


f = open(file,'a')
f.write(str(end_list))
f.close()

print(end_list)