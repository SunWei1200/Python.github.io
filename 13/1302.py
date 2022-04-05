#计算器
from tkinter import *
import tkinter

def add():
        a= eval(ent1.get())
        b= eval(ent2.get())
        z = "{:.2f}+{:.2f}={:.2f}\n".format(a,b,a+b)
        txt.insert(END, z)
        ent1.delete(0, END)
        ent2.delete(0, END)
def sub():
        a = eval(ent1.get())
        b = eval(ent2.get())
        z = "{:.2f}-{:.2f}={:.2f}\n".format(a, b, a - b)
        txt.insert(END,z)
        ent1.delete(0, END)
        ent2.delete(0, END)
def mul():
    a = eval(ent1.get())
    b = eval(ent2.get())
    z = "{:.2f}*{:.2f}={:.2f}\n".format(a, b, a * b)
    txt.insert(END, z)
    ent1.delete(0, END)
    ent2.delete(0, END)
def div():
    a = eval(ent1.get())
    b = eval(ent2.get())
    z = "{:.2f}/{:.2f}={:.2f}\n".format(a, b, a /b)
    txt.insert(END, z)
    ent1.delete(0, END)
    ent2.delete(0, END)

root=Tk()
root.title("计算器")
root.geometry('500x500')
ent1=Entry(root)
ent1.grid(row=0, column=0)
ent2=Entry(root)
ent2.grid(row=1, column=0)
btn1=Button(root,text = "加法",command = add)
btn1.grid(row=2, column=0)
btn2=Button(root,text = "减法",command = sub)
btn2.grid(row=3, column=0)
btn3 = Button(root, text="乘法", command=mul)
btn3.grid(row=4, column=0)
btn4 = Button(root, text="除法", command=div)
btn4.grid(row=5, column=0)
txt=Text(root)
txt.grid(row=6,column=0)
root.mainloop()

