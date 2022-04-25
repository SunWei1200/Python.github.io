#读入score.txt文件，统计每个年级的平均成绩存在问题
import jieba
path1="score.txt"
f1=open(path1,'r',encoding='utf-8')
a={}
next(f1)
for line1 in f1.readlines():
    a=0.0
    b=0.0
    id=[]
    grade=[]
    score1=[]
    score2=[]
    new_line= line1.strip().split()
    id.append(int(new_line[2]))
    score1.append(float(new_line[1]))
    score2.append(float(new_line[2]))
    grade.append(int(new_line[2]))
    i=0
    for i in range(9):
        if grade[i]==2:
            a=a+score1[i]+score2[i]

        else:
            b=b+score1[i]+score2[i]
    ave1=(a)/20
    ave2=b/20
print("二年级平均成绩".format(ave1))
print("三年级平均成绩".format(ave2))
f1.close()