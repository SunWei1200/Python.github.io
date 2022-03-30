#标签示例
from tkinter import *
root=Tk()
lb=Label(root,text="我是一个标签",
         bg='blue',
         fg='red',
         font=('楷体',32),
         width=20,
         height=2,
         relief=SUNKEN)
lb.pack()
root.mainloop()