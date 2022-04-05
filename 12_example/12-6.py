class STUDENT:
    def eat(self,name, place):
        print("{}在{}吃饭".format(name, place))

    def sleep(self,name, place):
        print("{}在{}睡觉".format(name, place))

    def gotoclass(self,name, place, class_name):
        print("{}在{}上{}课".format(name, place, class_name))

    def dosport(self,name, place, sport_name):
        print("{}在{}{}".format(name, place, sport_name))

    def study(self,name, place):
        print("{}在{}自习".format(name, place))

    def makeup(self,name, place):
        print("{}在{}化妆".format(name, place))

    def playgame(self,name, place, game_name):
        print("{}在{}玩{}".format(name, place, game_name))

    def watchvideo(self,name, video):
        print("{}在看{}".format(name, video))

if __name__=="__main__":
    student_name1="小明"
    student_class=STUDENT()
    print("================={}的一天=================".format(student_name1))
    student_class.eat(student_name1, "一食堂")
    student_class.gotoclass(student_name1, "一教", "python")
    student_class.dosport(student_name1, "操场", "篮球")
    student_class.study(student_name1, "图书馆")
    student_class.sleep(student_name1, "2号楼")