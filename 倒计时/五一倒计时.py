import time
import datetime
import tkinter

windows = tkinter.Tk()
windows.title('五一回家倒计时 --王汉')
windows.geometry('250x450')

def get_time():
    t0 = datetime.datetime.now()
    t1 = datetime.datetime(t0.year,t0.month,t0.day,t0.hour,t0.minute,t0.second)
    t2 = datetime.datetime(2020,4,30,18,00,00)

    days = (t2 - t1).days
    time1 = (t2-t1).seconds
    hours = (time1)//3600
    mins = (time1-hours*3600)//60
    sec = time1-hours*3600-mins*60

    time_text = "距离五一放假还有"+str(days)+'天'+str(hours)+'时'+str(mins)+'分'+str(sec)+'秒'
    return time_text
file1 = 'C:/Users/Dell/Desktop/tup1.jpg'

'''def get_image(file):
    i = tkinter.Entry.get(self=windows)
    im = Image.open(file)
    global tkimg
    tkimg = ImageTK.PhotoImage(im)

    label1 = tk.Label(windows,image=tkimg)
    label1.pack()
'''
'''photo = tkinter.PhotoImage(file = 'C:/Users/Dell/Desktop/tup1.gif')
l1 = tkinter.Label(windows,text='五一倒计时',compound = 'center',font = ('微软雅黑',20),image=photo)
l1.pack()'''

photo = tkinter.PhotoImage(file = 'C:/Users/Dell/Desktop/tup1.gif')
l1 = tkinter.Label(windows,text='五一倒计时',compound = 'center',font = ('微软雅黑',20),image=photo).pack()
def updateTime():
    time_text = get_time()
    l2 = tkinter.Label(windows,text=time_text,font=('Arial',12))
    l2.pack()
#按钮
b1 = tkinter.Button(windows,text='更新时间',command= updateTime,background = '#FFD700',compound = 'center',height='3',width='7')
b1.pack()


windows.mainloop()