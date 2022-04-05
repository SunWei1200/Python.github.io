class ANIMAL:
    def eat(self,zhonglei,name):
        print("{}{}在吃".format(zhonglei,name))
    def jump(self,zhonglei,name):
        print("{}{}在跳".format(zhonglei,name))

class CAT(ANIMAL):
    def maiomiaobark(self,zhonglei,name):
        print("{}{}在喵喵叫".format(zhonglei,name))

if __name__=="__main__":
    cat_zhonglei1="小白猫"
    cat_zhonglei2 = "小红猫"
    cat_zhonglei3 = "小蓝猫"
    cat_class1=CAT()
    cat_class1.maiomiaobark(cat_zhonglei1,"doudou")
    cat_class1.maiomiaobark(cat_zhonglei2,"maomao")
    cat_class1.maiomiaobark(cat_zhonglei3,"xiaohei")
    cat_class1.jump(cat_zhonglei3,"xiaohei")
    cat_class1.eat(cat_zhonglei2,"maommao")