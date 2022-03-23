#一次input()获得多个值
student_names=input("请输入学生列表，用英文逗号(,)分割")
print(student_names)
student_list=student_names.split(",")
print(student_list)