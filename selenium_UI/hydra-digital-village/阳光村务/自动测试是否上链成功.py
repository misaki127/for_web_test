#encoding:utf-8

import requests
import json
import pymysql
import io

connection = pymysql.connect(host="192.168.2.214", user="jgw", password="Jgw*31500-2018.6",
                             db="hydra_digital_village", charset='utf8mb4', port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql1 = "SELECT household_id FROM hydra_digital_village.t_family_information WHERE organization_id = '1a1b21c82262493b83777777222f0a9f';"
cursor.execute(sql1)
mysql = cursor.fetchall()
cursor.close()


file = 'D:/Hash3.txt'
f = open(file,'a')

for i in range(len(mysql)):
    str1 = "householdId=" + mysql[i]["household_id"]
    url = "https://digitalvillage.kf315.net/apiInterface/digital-village/hydra-digital-village/api/v1/block-chain-record/getChain?" + str1



    try:
        r = requests.get(url,timeout = 30)
        searchurl = json.loads(r.text)
        url2 = searchurl


        txHash =searchurl["results"]["txHash"]
        url3 = "http://blockchain.gw.kf315.net/informationDetail/getTxDetail?channelName=evidencechannel&txHash=" + txHash + "&_=1590473189806"#交易哈希
        p = requests.get(url3,timeout=30)
        json1 = json.loads(p.text)

        json2 = {"blockNum":searchurl["results"]["blockNum"],"blockHash":searchurl["results"]["blockHash"],"txHash":searchurl["results"]["txHash"]}#,"timestamp":searchurl["results"]["timestamp"]}
        json3 = {"blockNum":json1["data"]["results"]["blockNum"],"blockHash":json1["data"]["results"]["blockHash"],"txHash":json1["data"]["results"]["txHash"]}#,"timestamp":json1["data"]["results"]["txTime"]}
        if json2==json3:
            f.write(mysql[i]["household_id"] +"success")
        else:
            f.write(str(json2) + ";"+ str(json3))
        f.write("\n")
    except:
        f.write("请求失败")


f.close()
