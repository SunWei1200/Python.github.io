#BMI值计算
#分别输入身高和体重，输出BMI值，并保留1位小数
height=float(input("请输入您的身高（单位为米）："))
print("您的身高：",height,'m')
weight=float(input("请输入您的体重（单位为千克）："))
print("您的体重：",weight,'kg')
bmi = weight/(height*height)
print('你的BMI为：{0:.1f}'.format(bmi))