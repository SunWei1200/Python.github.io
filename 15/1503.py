#使用tkinter库，创建600*600的画布，以红色实线绘制坐标轴。当a=80,t在−π~π范围内以步长0.01变化时，用蓝色绘制函数图形。效果如图所示
#x=a(2sint −sin2t)
#y=a(2cost−cos2t)
from tkinter import *
import math
root=Tk()
w=Canvas(root,width=600,height=600)
w.pack()
w.create_line(0,300,600,300,fill='red',dash=(4,4))
w.create_line(300,0,300,600,fill='red',dash=(4,4))
w0=300
h0=300
a=80
def x(t):
    x=a*(2*math.sin(t)-math.sin(2*t))
    x+=w0
    return x
def y(t):
    y= a* (2*math.cos(t) -  math.cos(2*t))
    y-=h0
    y=-y
    return y
t=-math.pi
while(t<math.pi):
    w.create_line(x(t), y(t), x(t + 0.01), y(t + 0.01), fill='blue')
    t += 0.01
root.mainloop()