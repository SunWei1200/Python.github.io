#编写程序，通过循环计算全部水仙花数，并依次输出。
# 水仙花数是一个三位数字，该数字等于组成该三位数的各位数字的立方和。
# 例如13+53+33=153
# 方法一
sum = 0
print("所有的3位水仙花数:")
for x in range(100, 1000):
    s = str(x)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if x == a ** 3 + b ** 3 + c ** 3:
        print(x)