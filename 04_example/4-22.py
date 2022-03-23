#击鼓传花游戏
import random
import time
player_list=["Carol","Ann","Bob","Eve","Grace","Minica","Frank","Heidi","Judy"]
print("游戏开始，共有{}个玩家".format(len(player_list)))
print("他们分别是{}".format(",".join(player_list)))
print("请大家按照顺序排成一个圈")
player_list.sort()
print("ok排好序了，{}\n".format(player_list))

count=0
while (len(player_list)>1):
    count+=1
    print("第{}轮开始，花在{}手上".format(count,player_list[0]))
    print("开始击鼓喽")
    bad_luck_number=random.randint(0,len(player_list)-1)

    print("咚"*bad_luck_number)

    bad_guy_name=player_list.pop(bad_luck_number)

    print("鼓声停了，一共敲了{}下，花在{}手上，可怜的{}被淘汰了".format(bad_luck_number,bad_guy_name,bad_guy_name))

    print("剩下{}名玩家，它们是{}\n".format(len(player_list),player_list))
    time.sleep(3)
else:
    luck_guy_name=player_list.pop()

    print("最后的胜利者是{}，让我们恭喜他".format(luck_guy_name))