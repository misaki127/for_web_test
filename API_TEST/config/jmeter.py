import io
import requests
import time
import threading

url = 'http://192.168.2.215:10098/hydra-digital-village/api/v1/market-activity/addActivityRecord'
json1 = {'householdId':'748a832416694c4e8a5b166ac4c82480',
	'openId':'1'}

file = "D:/ceshi.txt"
headers = {"Content-Type":'application/x-www-form-urlencoded;charset=UTF-8'}
f = open(file,'a+')
list_t = []
def getmarket(url,i,headers,f,json1):
	json1['openId'] = i
	r = requests.post(url,data=json1,headers=headers)
	t = r.elapsed.total_seconds()
	f.write(str(r.text))
	f.write('\n')
	f.write(str(t))
	f.write('\n')
	localtime = time.asctime(time.localtime(time.time()))
	f.write(str(localtime))

	f.write('\n')
	'''
	print (r.text)
	return t'''

def ces(a,f):
	f.write(str(a))
	f.write('\n')
	localtime = time.asctime(time.localtime(time.time()))
	f.write(str(localtime))
	f.write('\n')

#多次访问接口
for i in range(1,51):
	json1['openId'] = i
	t = getmarket(url,i,headers,f,json1)
	list_t.append(t)


#并发访问
'''
thread = []
for i in range(1,51):

	exec('t{0} = threading.Thread(target=getmarket,args=(url,i,headers,f,json1))'.format(i))
	exec('thread.append(t{0})'.format(i))

	exec('t{0} = threading.Thread(target=ces,args=(i,f))'.format(i))
	exec('thread.append(t{0})'.format(i))

for t in thread:
	t.setDaemon(True)
	t.start()

for i in thread:
	t.join()
print("finall")

'''

f.close()
