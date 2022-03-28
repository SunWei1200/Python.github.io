#读入score.txt文件，统计每个班级的不及格人数
import pandas as pd
path1="score.txt"
f1=open(path1,'r',encoding='utf-8')
a=0
b=0
next(f1)
for line1 in f1.readlines():
    newline1 = line1.rstrip()
    newwords1=newline1.split(" ")
    print(newwords1)
    id=newwords1[0]
    score1=int(newwords1[1])
    score2=int(newwords1[2])
    grade=newwords1[3]
    newgrade = newwords1.groupby(grade)
    print(newgrade)
    if score1<60:
        a=a+1
    if score2<60:
        b=b+1
f1.close()
