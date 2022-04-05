class ANIMAL:
    def eat(self,zhonglei,name):
        print("{}{}在吃".format(zhonglei,name))
    def jump(self,zhonglei,name):
        print("{}{}在跳".format(zhonglei,name))

class CAT(ANIMAL):
    def maiomiaobark(self,zhonglei,name):
        print("{}{}在喵喵叫".format(zhonglei,name))

class DOG(ANIMAL):
    def wangwangbark(self,zhonglei,name):
        print("{}{}在汪汪叫".format(zhonglei, name))

if __name__=="__main__":
    cat_zhonglei1="小黑猫"
    dog_zhonglei1="小黄狗"
    cat_class1=CAT()
    dog_class1=DOG()
    cat_class1.maiomiaobark(cat_zhonglei1,"doudou")
    cat_class1.jump(cat_zhonglei1,"xiaohei")
    cat_class1.eat(cat_zhonglei1,"maommao")
    dog_class1.wangwangbark(dog_zhonglei1,"dahuang")
    dog_class1.eat(dog_zhonglei1,"dahuang")