#读入学生名单
#读入学生名单并保存为字典。并实现输入学生学号，返回学生姓名
path1="students.txt"
student_dict={}
f1=open(path1,'r')
for line1 in f1.readlines():
    newline1 =line1.rsplit()
    newwords1= newline1[0].split(",")
    sid,sname= newwords1
    student_dict[sid]=sname
f1.close()
while True:
    newsid=input("请输入学生学号：")
    if newsid in student_dict:
        print("学生姓名为{}".format(student_dict[newsid]))
    else:
        print("该学号不存在")