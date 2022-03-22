#编写程序，开发一个循环5次计算的小游戏，每次随机产生两个100以内的数字，
# 让用户计算两个数字之和并输入结果，
# 如果计算结果正确则加一分，如果计算结果错误则不加分。
# 如果正确率大于等于80%，则闯关成功

import random
print("欢迎来到猜数游戏")
#设置次数，循环五次，默认进入程序就是第一次
count = 1
#设置一个变量用于统计用户计算对的次数
acount = 0
while count<=5:
    #执行一次，次数加一
    count = count+1
    # 声明两个在1-10之间产生随机数
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print(number1)
    print(number2)
    temp = int(input())
    result= number1 + number2
    print("实际的运算结果是:",result)
    #如果计算正确了，则acount加1
    if temp == result:
        acount = acount+1
#五次循环以后游戏结束
print("游戏结束,你猜对了",acount,"次")
#计算用户猜对的比例
if acount/5>=0.8:
    print("闯关成功")
else:
    print("闯关不成功")


