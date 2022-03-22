#编写程序，从键盘输入数字n，通过循环计算1~n的乘积
def recursion_fun(integer):
    if integer == 0:
        return 1
    return integer * recursion_fun(integer - 1)


n = int(input('请输入一个整数n:'))
print(recursion_fun(n))