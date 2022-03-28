#根据分隔符进行分割，返回值为列表
path1="students.txt"
f1=open(path1,'r')
for line1 in f1.readlines():
    newline1=line1.rsplit()
    newwords1=newline1[0].split(",")
    print(
        newwords1
    )
f1.close()
