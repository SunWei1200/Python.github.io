#中断循环
import random
games=10
for i in range(games):
    print("进行第{}场游戏".format(i+1))
    feeling=random.randint(0,10)
    if 5<=feeling<=9:
        print("中断本次游戏，开始下一局")
        continue
    elif feeling==10:
        print("中断游戏，不玩了")
        break
    else:
        print("玩得很开心")
    result=random.randint(0,1)
    if result==1:
        print("朋友圈炫耀战绩")
    else:
        print("沉默")
    print("*"*20)
