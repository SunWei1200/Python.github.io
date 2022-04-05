#计算器
from tkinter import *
import tkinter
class Jisuanqi():
    def __init__(self, a, b):
        a=self.ent1
        b=self.ent2
        self.ent1=Entry()
        self.ent1.grid(row=0, column=0)
        self.ent2=Entry()
        self.ent2.grid(row=0, column=1)
        a=eval(self.ent1.get())
        b=eval(self.ent2.get())
        self.btn1=Button(root,text = "加法",command = self.add)
        self.btn1.grid(row=0, column=2)
        self.btn2=Button(root,text = "减法",command = self.sub)
        self.btn2.grid(row=0, column=3)
        self.btn3 = Button(root, text="乘法", command=self.mul)
        self.btn3.grid(row=0, column=4)
        self.btn4 = Button(root, text="除法", command=self.div)
        self.btn4.grid(row=0, column=4)
        txt.insert(END,self)
        a.delete(0,END)
        b.delete(0, END)
    def add(self):
        z = int(self.ent1) +int(self.ent2)
    def sub(self):
        z = int(self.ent1) -int(self.ent2)
    def mul(self):
        z = int(self.ent1) *int(self.ent2)
    def div(self):
        z = int(self.ent1) /int(self.ent2)

root=Tk()
root.title("计算器")
root.geometry('500x500')
jisuan=Jisuanqi(root)
txt=Text(root)
txt.pack()
root.mainloop()

