#读入score.txt文件，统计每个年级的平均成绩
import jieba
path1="score.txt"
f1=open(path1,'r',encoding='utf-8')
a={}
next(f1)
for line1 in f1.readlines():
    newline1 = line1.rstrip()
    newwords1 = newline1.split(" ")
    score1,score2,grade=newwords1[1:]


f1.close()