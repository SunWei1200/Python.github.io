from tkinter import *
def run1():
    s1=s2=""
    if var1.get()==11:
        s1="男"
    else:
        s1="女"
    if var2.get()==33:
        s2="大一"
    elif var2.get()==44:
        s2 = "大二"
    elif var2.get()==55:
        s2 = "大三"
    else:
        s2 = "大四"
    s="hello,{}{}".format(s2,s1)
    lb2.configure(text=s)

root=Tk()
root.title("TEST")
root.geometry("300x300")
lb1=Label(root,text="请选择性别和年级")
lb1.pack()

var1=IntVar()
var2=IntVar()
rb1=Radiobutton(root,text="男",variable=var1,value=11)
rb1.pack()
rb2=Radiobutton(root,text="女",variable=var1,value=22)
rb2.pack()
rb3=Radiobutton(root,text="大一",variable=var2,value=33)
rb3.pack()
rb4=Radiobutton(root,text="大二",variable=var2,value=44)
rb4.pack()
rb5=Radiobutton(root,text="大三",variable=var2,value=55)
rb5.pack()
rb6=Radiobutton(root,text="大四",variable=var2,value=66)
rb6.pack()
btn=Button(root,text="按钮",command=run1)
btn.pack()
lb2=Label(root,text="")
lb2.pack()
root.mainloop()



#单选按钮（Radiobutton）是为响应互相排斥的若干单选项的单击事件以触发运行自定义函数所设的，
# 该控件除具有共有属性外，还具有显示文本（text）、返回变量（variable）、返回值（value）和响应函数名（command）等重要的属性
#variable用来分组，不同组variable的值不同
#value用来区分同一组中不同的选项
