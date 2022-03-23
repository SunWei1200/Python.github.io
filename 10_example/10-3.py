#读入全部文本内容，返回结果为一个列表
#列表中的每个元素为一行文本字符串
path1="lemontree.txt"
f1=open(path1,'r')
content3=f1.readlines()
print(content3)
f1.close()
