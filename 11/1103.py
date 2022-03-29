#姓名缘分。
#输入：你的姓名，恋人姓名
#输出：缘分情况
import random
def yuanfen(yourname,lovername):
    count=0
    for i in yourname:
        count+=ord(i)
    for j in lovername:
        count+=ord(j)
    random.seed(count)
    a=random.randint(1,100)
    if a>=0 and a<60:
        print("毫无缘分")
    elif a>=60 and a<70:
        print("有缘无分")
    elif a>=70 and a<80:
        print("合适")
    elif a>=80 and a<90:
        print("般配")
    elif a>=90 and a<100:
        print("佳缘")
    elif a==100:
        print("天作之合")
    return a

while True:
  yourname=input("输入你的姓名：")
  lovername=input("恋人姓名：")
  a=yuanfen(yourname,lovername)
  print("{}和{}是{}".format(yourname,lovername,a))

