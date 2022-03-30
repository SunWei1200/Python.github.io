#文本框举例
#每隔1秒取一次当前日期时间，并写入文本框中。
# 本例中调用datetime.now()获取当前日期时间，
# 用insert()方法每次从文本框txt的尾部（END）开始追加文本

from tkinter import *
import datetime
def gettime():
    s="{}\n".format(str(datetime.datetime.now()))
    txt.insert(END,s)
    root.after(1000,gettime)

root=Tk()
root.geometry('320x240')
txt=Text(root)
txt.pack()
gettime()
root.mainloop()