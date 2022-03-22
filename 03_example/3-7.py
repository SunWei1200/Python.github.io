#计算π的近似值
import math
n=1
t=1
total=0
flag=1
count=0
while math.fabs(t)>=1e-6:
    total+=t
    flag=-flag
    n+=2
    t=flag*1.0/n
    count+=1
    print("count{},π={}".format(count,total*4))
