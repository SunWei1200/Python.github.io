#每次循环读取文件的一行

path1="lemontree.txt"
f1=open(path1,'r')
for line1 in f1.readlines():
    print(
        line1
    )
f1.close()
