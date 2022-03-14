# 题目：
# 某个公司采用公用电话传递数据，
# 数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：
# 每位数字都加上5,
# 然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
a = input("请输入四位数字：")
a_list = []
for i in range(4):
    a_list.append(int(a[i]))

for j in range(4):
    a_list[j] = (a_list[j] + 5) % 10

a_list[0], a_list[3] = a_list[3], a_list[0]
a_list[1], a_list[2] = a_list[2], a_list[1]

for k in range(4):
    print(a_list[k], end='')
