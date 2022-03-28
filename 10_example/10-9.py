#将数据写入文件
path2="students2.txt"
f=open(path2,'w')
f.write("181100001,")
f.write("Alice")
f.write("\n")
f.write("181100002,Bob\n")
f.close()