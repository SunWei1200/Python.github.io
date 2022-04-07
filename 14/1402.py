#error
import tkinter
from tkinter import *
import tkinter.messagebox
def order():
    s1=s2=s3=s4=""
    z=0
    if var1.get()==1:
        s1="汉堡包"
        z=z+12
    if var2.get()==1:
        s2="蛋挞"
        z=z+7
    if var3.get()==1:
        s3="猪肉卷"
        z=z+10
    if var4.get()==1:
        s4="饮料"
        z=z+5
    s="您点了{}{}{}{}".format(s1,s2,s3,s4)
    q= "一共{}元".format(z)
    lb2.configure(text=s)
    lb3.configure(text=q)
    answer = tkinter.messagebox.askokcancel("会员付款界面", "请输入会员码")

    if answer:
        c = z * 0.8
        lb2.configure(text="折扣价为{}元".format(c))
    else:
        lb2.configure(text="")

def count():
    s1 = s2 = s3 = s4 = ""
    z = 0
    if var1.get() == 1:
        s1 = "汉堡包"
        z = z + 12
    if var2.get() == 1:
        s2 = "蛋挞"
        z = z + 7
    if var3.get() == 1:
        s3 = "猪肉卷"
        z = z + 10
    if var4.get() == 1:
        s4 = "饮料"
        z = z + 5
    answer = tkinter.messagebox.askokcancel("会员付款界面", "请输入会员码")
    if answer:
        c = z * 0.8
        lb.configure(text="折扣价为{}元".format(c))
    else:
        lb.configure(text="")
    p=eval(ent1.get())
    t=p-z
    r="收您{}元，找零{}元".format(p,t)
    lb4.configure(text=r)

root=tkinter.Tk()
root.title("自助点餐")
lb=tkinter.Label(root,text="您好，请问需要什么？")
lb.pack()
var1=tkinter.IntVar()
var2=tkinter.IntVar()
var3=tkinter.IntVar()
var4=tkinter.IntVar()
ch1=tkinter.Checkbutton(root,text="汉堡包：12元",variable=var1,onvalue=1,offvalue=0)
ch1.pack()
ch2=tkinter.Checkbutton(root,text="蛋挞：7元",variable=var2,onvalue=1,offvalue=0)
ch2.pack()
ch3=tkinter.Checkbutton(root,text="猪肉卷：10元",variable=var3,onvalue=1,offvalue=0)
ch3.pack()
ch4=tkinter.Checkbutton(root,text="饮料：5元",variable=var4,onvalue=1,offvalue=0)
ch4.pack()
btn=tkinter.Button(root,text="OK",command=order)
btn.pack()
lb2=tkinter.Label(root,text="")
lb2.pack()
lb3=tkinter.Label(root,text="")
lb3.pack()
ent1=Entry(root)
ent1.pack()
btn=tkinter.Button(root,text="付款",command=count)
btn.pack()
lb4=tkinter.Label(root,text="")
lb4.pack()
root.mainloop()