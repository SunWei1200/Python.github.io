#用pack()方法不加参数排列标签
#为看清楚各控件实例所占用的空间大小，文本使用了不同长度的中英文，
# 并设置relief=GROOVE的凹陷边缘属性
from tkinter import *
root=Tk()
lbred=Label(root,text="Red",fg="red",relief=GROOVE)
lbred.pack()
lbgreen=Label(root,text="green",fg="green",relief=GROOVE)
lbgreen.pack()
lbblue=Label(root,text="BLUE",fg="blue",relief=GROOVE)
lbblue.pack()
root.mainloop()