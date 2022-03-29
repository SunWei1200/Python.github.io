#使用函数实现，按照1美元=6人民币汇率编写一个美元和人民币的双向兑换程序
def RMB2Dollar(yuan):
    dollar=6*eval(yuan)
    return dollar
def Dollar2RMB(dollar):
    yuan=eval(dollar)/6
    return yuan

yuan1=input("请输入金额（元）：")
dollar1=RMB2Dollar(yuan1)
print("转化为{}美元".format(dollar1))
dollar2=input("请输入金额（美元）：")
yuan2=Dollar2RMB(dollar2)
print("转化为{}元".format(yuan2))