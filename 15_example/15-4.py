#以5像素笔触重复执行“前进100像素，
# 右转60度”的操作共6次，绘制红色正六边形；
# 再用circle()方法画半径为60像素的红色圆内接正六边形；
# 然后抬笔移动至（-50,200）点落笔，重复执行“右转144度，
# 前进400像素”的操作共5次，绘制五角星

from turtle import *
setup(900,900,0,0)
reset()
pensize(5)
for i in range(6):
    fd(100)
    right(60)
color('red')
circle(60,steps=6)
up()
goto(-50,200)
down()
for i in range(5):
    right(144)
    fd(400)
done()
