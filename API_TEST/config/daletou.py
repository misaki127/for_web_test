import random
import time

list0 = []
success = 0
while success < 7:
    str1 = input("请输入你要买的大乐透号码，用空格分隔,前面五个为1-35，后面2个为1-12")
    list3 = str1.split()
    if len(list3) >= 7:
        for p in list3:
            list0.append(int(p))
        for i in range(5):
            if list0[i] >= 1 and list0[i] <= 35:
                success += 1
            else:
                pass
        for f in range(5,7):
            if list0[f] >= 1 and list0[f] <= 12:
                success += 1
            else:
                pass
        if success < 7:
            print("输入有误，请重新输入！")
        else:
            pass
    else:
        print("请重新输入！")

list1 = [[],[]]
for i in range(5):
    a = random.randint(1,35)
    list1[0].append(a)

for i in range(2):
    a = random.randint(1,12)
    list1[1].append(a)

list2 = [[list0[0],list0[1],list0[2],list0[3],list0[4]],[list0[5],list0[6]]]
a = [x for x in list2[0] if x in list1[0]]
b = [y for y in list2[1] if y in list1[1]]
if a == 5 :
    if b == 0 :
        print("恭喜你获得三等奖")
    elif b == 1:
        print("恭喜你获得二等奖")
    elif b == 2:
        print("恭喜你获得一等奖")
    else:
        print("服务错误！")
elif a == 4 :
    if b == 0 :
        print("恭喜你获得七等奖")
    elif b == 1:
        print("恭喜你获得五等奖")
    elif b == 2:
        print("恭喜你获得四等奖")
    else:
        print("服务错误！")
elif a == 3 :
    if b == 0 :
        print("恭喜你获得九等奖")
    elif b == 1:
        print("恭喜你获得八等奖")
    elif b == 2:
        print("恭喜你获得六等奖")
    else:
        print("服务错误！")
elif a == 2 :
    if b == 0 :
        print("您没中奖！")
    elif b == 1:
        print("恭喜你获得九等奖")
    elif b == 2:
        print("恭喜你获得八等奖")
    else:
        print("服务错误！")
elif a == 1:
    if b == 0 :
        print("您没中奖！")
    elif b == 1:
        print("您没中奖！")
    elif b == 2:
        print("恭喜你获得九等奖")
    else:
        print("服务错误！")
elif a == 0 :
    if b == 0 :
        print("您没中奖！")
    elif b == 1:
        print("您没中奖！")
    elif b == 2:
        print("恭喜你获得九等奖")
    else:
        print("服务错误！")
else:
    print("您没中奖！")
print("开奖号码为：" + str(list1))
time.sleep(10)