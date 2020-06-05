#encoding:utf-8

import os
import time


print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
def run():
    t = 60
    os.system("python ./三资管理.py")
    time.sleep(t)
    os.system("python ./优秀党员.py")
    time.sleep(t)
    os.system("python ./党员学习.py")
    time.sleep(t)
    os.system("python ./党组织管理.py")
    time.sleep(t)
    os.system("python ./决策公示.py")
    time.sleep(t)
    os.system("python ./孤寡老人扶助.py")
    time.sleep(t)
    os.system("python ./工作动态.py")
    time.sleep(t)
    os.system("python ./我家宝贝.py")
    time.sleep(t)
    os.system("python ./村民表彰.py")
    time.sleep(t)
    os.system("python ./残疾人扶助.py")
    time.sleep(t)
    os.system("python ./民生公示-低保五保.py")
    time.sleep(t)
    os.system("python ./民生公示-危房改造.py")
    time.sleep(t)
    os.system("python ./民生公示-大病救助.py")
    time.sleep(t)
    os.system("python ./民生公示-留守儿童.py")
    time.sleep(t)
    os.system("python ./组织建设.py")
    time.sleep(t)
    os.system("python ./责任组管理.py")
    time.sleep(t)
    os.system("python ./贫困户评定.py")
    time.sleep(t)
    os.system("python ./通知公告.py")
    time.sleep(t)
    os.system("python ./集体经济.py")
    time.sleep(t)
    os.system("python ./项目公开.py")
    time.sleep(t)
    print("测试完成。")



run()
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

