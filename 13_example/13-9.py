#加法器（2）

from tkinter import *
def run2(a,b):
    s="{:.2f}+{:.2f}={:.2f}\n".format(a,b,a+b)
    txt.insert(END,s)
    inp1.delete(0,END)
    inp2.delete(0, END)

root=Tk()
root.title("加法器")
root.geometry('500x500')
lb1=Label(root,text="请输入两个数，按下面按钮进行加法计算")
lb1.pack()
inp1=Entry(root)
inp1.pack()
inp2=Entry(root)
inp2.pack()
btn1=Button(root,text="加法",command=lambda :run2(eval(inp1.get()),exec(inp2.get())))
btn1.pack()
txt=Text(root)
txt.pack()
root.mainloop()