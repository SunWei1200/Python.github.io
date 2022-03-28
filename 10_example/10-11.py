#词频统计
path1="lemontree.txt"
f1=open(path1,"r")
content=f1.read()#读取文件内容，返回一个字符串
content=content.lower()#将字符串中所有的字母小写
for ch in [',',':','.']:
    content=content.replace(ch," ")#将文本中特殊字符替换为空格
words=content.split()
counts={}

for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{}==={}".format(word,count))