#在320×240的窗体上创建高200像素，宽300像素的画布，
# 鼠标单击画布，依次绘出：从（90,10）到（200,200）点的矩形；
# 从（90,10）到（200,200）点的内切椭圆并填充绿色；
# 从（90,10）到（200,200）点的内切扇形并填充粉红色；
# 连接（20,180）、（150,10）和（290,180）三点形成蓝色框线且无色填充的三角形；
# 从（10,105）到（290,105）点的红色直线；
# 以（50,10）为起点用RGB"#123456"颜色绘制文本标签“我的画布”。
# 单击“清空”按钮删除所有图形
from tkinter import *
def draw(event):
    mycanvas.create_rectangle(90,10,200,200)
    mycanvas.create_oval(90,10,200,200,fill='green')
    mycanvas.create_arc(90,10,200,200,fill='pink')
    mycanvas.create_polygon(20,180,150,10,290,180,outline='blue',fill='')
    mycanvas.create_line(10,105,290,105,fill='red')
    mycanvas.create_text(50,10,text='我的画布',fill='#123456')
def delt():
    mycanvas.delete(ALL)


root=Tk()
root.geometry('320x240')
mycanvas=Canvas(root,width=300,height=200)
mycanvas.bind('<ButtonPress-1>',draw)
mycanvas.pack()
btnclear=Button(root,text='清空',command=delt)
btnclear.pack()
root.mainloop()