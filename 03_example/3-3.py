#统计字符数出现次数
word='山羊上山山碰山羊角'
sum=0
for letter in word:
    if letter=="山":
        sum+=1
    print(sum)
