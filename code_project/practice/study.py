# import math
# a=1
# b=9
# c=20
# x=b**2-4*a*c
# print((-b+math.sqrt(x))/(2*a))
# print(math.log2(8))
# print("logdsa"[3])

# weight=float(input("体重:"))
# height=float(input("身高:"))
# BMI=weight/height**2
# print("你的BMI值为："+str(BMI))
# print("你今年"+input("年龄：")+"岁了")

# if 5*3>int(input("值：")):
#     print("True")
# else:
#     print("False")
# print("你好，懒洋洋")

# weight=float(input("体重:"))
# height=float(input("身高:"))
# BMI=weight/height**2
# xingbie=input("您的性别为：")
# print("你的BMI值为：" + str(BMI))
# if BMI<=18.5:
#     if xingbie=="man"or"男":
#         print("先生您偏瘦")
#     else:
#         print("女士您偏瘦")
# elif 18.5<BMI<=25:
#     if xingbie=="man":
#         print("先生您正常")
#     else:
#         print("女士您正常")
# elif 25<BMI<=30:
#     if xingbie == "man":
#         print("先生您偏胖")
#     else:
#         print("女士您偏胖")
# else:
#     if xingbie == "man":
#         print("先生您肥胖")
#     else:
#         print("女士您肥胖")

# s="hello"
# print(s.upper())
# s=s.upper()
# print(s)
# print("hello".upper())

# shopping_list=[]
# shopping_list.append("键帽")
# shopping_list.append("音响")
# shopping_list.remove("键帽")
# shopping_list.append("电竞椅")
# shopping_list.append("鼠标")
# shopping_list[1]="键盘"
# print(len(shopping_list))
# print(shopping_list)
# print(shopping_list[0])

# price=[733,1024,200,800]
# max_price=max(price)
# min_price=min(price)
# sorted_price=sorted(price)
# print(max_price)
# print(min_price)
# print(sorted_price)

# slang_dict={"懒羊羊"and"悦":"蠢猪",
#             "YYDS"and"yyds":"永远的神"}
# slang_dict["双减"]="双休"
# query=input("请输入：")
# if query in slang_dict:
#     print("您查询的"+query+"含义如下")
#     print(slang_dict[query])
# else:
#     print("没有")
#     print("当前收入本词典词条数为:"+str(len(slang_dict))+"条。")
# print("悦=懒洋洋")
# print(slang_dict)
#懒羊羊" and "悦"：
# "懒羊羊" 是非空字符串，逻辑上为真。
# 返回 "悦"，因此字典的键是 "悦"。
# "YYDS" or "yyds"：
# "YYDS" 是非空字符串，逻辑上为真。
# 返回 "YYDS"，因此字典的键是 "YYDS"。
# and：返回第一个假值，如果没有假值，则返回最后一个真值
# or：返回第一个真值，如果没有真值，则返回最后一个假值

# slang_dict = {
#     "懒羊羊": "蠢猪",
#     "悦": "蠢猪",
#     "YYDS": "永远的神",
#     "yyds": "永远的神"
# }
# slang_dict["双减"] = "双休"
# query = input("请输入：")
# if query in slang_dict:
#     print("您查询的" + query + "含义如下")
#     print(slang_dict[query])
# else:
#     print("没有")
#     print("当前收入本词典词条数为:" + str(len(slang_dict)) + "条。")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体为黑体，支持中文
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 生成爱心的 x 和 y 坐标
def heart(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# 动态绘制爱心
def draw_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = heart(t)

    plt.ion()  # 开启交互模式
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.axis('off')  # 隐藏坐标轴

    for i in range(1, len(x) + 1):
        ax.plot(x[:i], y[:i], color='red')
        plt.pause(0.001)  # 动态更新
    
    # 在爱心内部添加文字
    ax.text(0, 0, "老妈", fontsize=20, color='red', ha='center')
    ax.text(0, -5, '母亲节快乐', fontsize=20, color='red', ha='center')
    plt.ioff()  # 关闭交互模式
    plt.show()

if __name__ == "__main__":
    draw_heart()