#消息对话框示例
from tkinter import *
import tkinter.messagebox
root=Tk()
def xz():
    answer=tkinter.messagebox.askokcancel('请选择','请选择确认或者取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')
lb=Label(root,text='')
lb.pack()
btn=Button(root,text='弹出对话框',command=xz)
btn.pack()
root.mainloop()