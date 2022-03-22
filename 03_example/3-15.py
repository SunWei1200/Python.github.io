#猜颜色
import random
point=random.randint(1,6)
count=1
while count<=3:
    guess=int(input("请输入您的猜测："))
    if guess>point:
        print("您的猜测偏大")
    elif guess<point:
        print("您的猜测偏小")
    else:
        print("恭喜您猜对了")
        break
    count=count+1
else:
    point("很遗憾，三次全猜错了")