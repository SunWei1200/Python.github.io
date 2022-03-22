#编写程序，从键盘输入a,b,c的值，计算一元二次方程ax^2+bx+c=0的根，
# 根据b^2−4ac的值大于0、等于0及小于0分别进行讨论
import math
a, b, c = (input('请输入a、b、c：').split())
a, b, c = int(a), int(b), int(c)
delta= b**2 - 4*a*c
if delta == 0:
    solution_equation = -b / (2*a)
    print('%.2f' % solution_equation, ' ', '%.2f' % solution_equation)
elif delta > 0:
    solution_equation_1 = (-b + math.sqrt(delta)) / (2*a)
    solution_equation_2 = (-b - math.sqrt(delta)) / (2*a)
    print('%.2f' % solution_equation_1, ' ', '%.2f' % solution_equation_2)
elif delta<0:
    print("无解！")