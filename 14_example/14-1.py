from tkinter import *
def Mysel():
    choice=var.get()
    choice_dict={0:'甲',1:'乙',2:'丙'}
    s="您选了{}项".format(choice_dict[choice])
    lb.configure(text=s)

root=Tk()
root.title("单选GUI")
root.geometry("200x200")
lb=Label(root)
lb.pack()
var=IntVar()
rd1=Radiobutton(root,text="甲",variable=var,value=0,command=Mysel)
rd1.pack()
rd2=Radiobutton(root,text="乙",variable=var,value=1,command=Mysel)
rd2.pack()
rd3=Radiobutton(root,text="丙",variable=var,value=2,command=Mysel)
rd3.pack()
root.mainloop()


#单选按钮（Radiobutton）是为响应互相排斥的若干单选项的单击事件以触发运行自定义函数所设的，
# 该控件除具有共有属性外，还具有显示文本（text）、返回变量（variable）、返回值（value）和响应函数名（command）等重要的属性
#variable用来分组，不同组variable的值不同
#value用来区分同一组中不同的选项
