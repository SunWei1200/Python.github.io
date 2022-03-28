#读入score.txt文件，统计每个年级一共有多少人
import jieba
path1="score.txt"
f1=open(path1,'r',encoding='utf-8')
a=0
b=0
next(f1)
for line1 in f1.readlines():
    newline1 = line1.rstrip()
    newwords1 = newline1.split(" ")
    grade = int(newwords1[3])
    print(grade)
    if grade==2:
         a=a+1
    elif grade==3:
         b=b+1
print("二年级有{}人".format(a))
print("三年级有{}人".format(b))
f1.close()

