#在列表中删除元素2
friend_list=["马云","马化腾","王健林","李彦宏"]
print("==============2016年生日==============")
print(friend_list)


print("=============2017年生日==============")
name1=friend_list.pop()
print("{},再见！".format(name1))
print(friend_list)

print("=============2018年生日==============")
name2=friend_list.pop(2)
print("{},再见！".format(name2))
print(friend_list)