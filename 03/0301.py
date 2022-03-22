#编写程序，产生两个10以内的随机整数，以第一个随机整数为半径，第二个随机整数为高，计算并输出圆锥体的体积
import random
r=random.randint(1,10)
h=random.randint(1,10)
print("半径：",r)
print("高：",h)

pi=3.1415926
v=(pi*(r*r)*h)/3
print("圆锥体体积：",v)