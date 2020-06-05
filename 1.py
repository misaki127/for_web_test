import random
import io


p = open("E:/text1.csv",mode = "a+")
p.write("姓名"+","+"电话号码"+ "," + "身份证号码")
list1 = []
for i in range(10):
	f = random.randrange(10000000000,19999999999)
	s = random.randrange(100000000000000000,999999999999999999)
	p.write("\n")
	for i in range(2):
		h = random.randrange(0x4E00, 0x9fbf)
		p.write(str(chr(h)))
	p.write(",")
	p.write(str(f))
	p.write(",")
	p.write(str(s))
	list1.append(f)
	list1.append(s)
	pass

p.close()
print(list1)


