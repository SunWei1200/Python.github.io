class STUDENT2:
    student_name=""
    def __int__(self,name):
        self.student_name=name
    def eat(self, place):
        print("{}在{}吃饭".format(self.student_name, place))

    def sleep(self, place):
        print("{}在{}睡觉".format(self.student_name, place))

    def gotoclass(self, place, class_name):
        print("{}在{}上{}课".format(self.student_name, place, class_name))

    def dosport(self, place, sport_name):
        print("{}在{}{}".format(self.student_name, place, sport_name))

    def study(self, place):
        print("{}在{}自习".format(self.student_name, place))

    def makeup(self, place):
        print("{}在{}化妆".format(self.student_name, place))

    def playgame(self, place, game_name):
        print("{}在{}玩{}".format(self.student_name, place, game_name))

    def watchvideo(self, video):
        print("{}在看{}".format(self.student_name, video))

if __name__=="__main__":
    student_name1="小明"
    student_class2=STUDENT2()
    print("================={}的一天=================".format(student_class2.student_name))
    student_class2.eat( "一食堂")
    student_class2.gotoclass( "一教", "python")
    student_class2.dosport( "操场", "篮球")
    student_class2.study("图书馆")
    student_class2.sleep("2号楼")