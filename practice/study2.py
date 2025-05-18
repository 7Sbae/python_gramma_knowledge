# jia_bing=["cyh","hc","mz"]
# print(jia_bing)
# print("希望{}能与我共进晚餐".format(jia_bing[1]),sep='')
# print(f"希望{jia_bing[0]}能与我共进晚餐",sep='')
# print("希望jia_bing[2]能与我共进晚餐",sep='')
# print(jia_bing[2],"不能与我共进晚餐")
# jia_bing[2]="pzt"
# print(jia_bing)
# jia_bing.append("y")
# jia_bing.insert(0,'lyy')
# jia_bing.insert(3,'cz')
# print(jia_bing)
# print("我只能邀请两位来与我共进晚餐")
# name1=jia_bing.pop()
# name2=jia_bing.pop(1)
# name3=jia_bing.pop(2)
# jia_bing.remove("pzt")
# print(jia_bing)
# del jia_bing[0]
# print(jia_bing)
# del jia_bing[0]
# print(jia_bing)

# sort()方法是用于对列表（list）进行排序的。sort()方法有一个可选参数reverse，用于指定排序的顺序。
# 当reverse=False（默认值）时，sort()方法将按升序（从小到大）对列表进行排序。
# 当reverse=True时，sort()方法将按降序（从大到小）对列表进行排序
car= ["bmw","audi","toyota","subaru"]
car.sort(reverse=True)
print(car)
