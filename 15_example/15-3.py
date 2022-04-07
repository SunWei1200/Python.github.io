#从原点出发至坐标点（-100,100），改为红色，
# 沿光标指向（默认方向为水平向右）前进200像素，改为蓝色，
# 后退100像素，以动画模式输出文字（黑体，36磅，斜体）

import turtle
turtle.setup(640,480,300,300)
turtle.reset()
turtle.pensize(5)
turtle.goto(-100,100)
turtle.color('red')
turtle.fd(200)
turtle.color('blue')
turtle.bk(100)
turtle.write('turtle绘图',move=True,font=('黑体',36,'italic'))