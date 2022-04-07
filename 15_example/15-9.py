#在320×240的窗体上创建画布，并以蓝色笔创建鼠标画板
from tkinter import *
root=Tk()
def move(event):
    x=event.x
    y=event.y
    w.create_oval(x,y,x+1,y+1,fill='blue')

w=Canvas(root,width=320,height=240)
w.pack()
w.bind('<B1-Motion>',move)
root.mainloop()