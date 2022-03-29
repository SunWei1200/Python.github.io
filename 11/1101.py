def waterrate(water):
    if water>0 and water<=220:
        cost=3.45*water
    elif water<220 and water<=300:
        cost=4.83*water
    elif water>300:
        cost=5.83*water
    else:
        print("输入错误")
    return cost

cost=waterrate(150)
print("总水费{}".format(cost))


