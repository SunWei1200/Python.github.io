#编写程序，判断一个整数是否为素数
# （判断整数x是否为素数，最简单的方法就是用2~x-1之间的所有整数逐一去除x，若x能被其中任意一个数整除，则x就不是素数，否则就为素数）
n = int(input())
for i in range(2, n):
    leap = 0
    if n % i == 0:
        leap = 1
        break
if leap == 0:
    print('Yes')
else:
    print('No')