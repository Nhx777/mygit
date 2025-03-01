'''
a=input("请输入字符串:")
print("zifuchuandechangduwei",len(a))

a=input("请输入字符串1：")
b=input("请输入字符串2:")
if a in b:
    print(f"'{a}'是'{b}'的子串")
else:
    print("不是子串")

a=input("请输入字符串:")
b=input("请输入字符串:")
result=a+b
print(result)

a=input("请输入字符串:")
key=666
b=int(input())
if b == (key()):
    print(a)
else:
    print("不许看")

print("------计算卡路里------")
weight=int(input("请输入体重（kg）"))
speed=int(input("请输入速度（m/s）"))
time=int(input("请输入时间（min）"))
print("消耗的卡路里=",weight*time*(30/speed))

N=float(input("输入一个小鼠："))
m=int(N)
b=abs(N-m)
print("整数部分为：",m,"小数部分为：",b)

num=int(input("请输入一个三位数"))
b,s,g=(num//100,num//10%10,num%10)
b,g=g,b
print(b,s,g,sep="")
'''
'''
a=int(input("请输入一个第一条边"))
b=int(input("请输入一个第二条边"))
c=int(input("请输入一个第三条边"))
new=[a,b,c]
new.sort()
if new[0]+new[1]>new[2]:
    print("可以组成三角形")
else:
    print("不能组成三角形")

import random
a=random.randint(1,100)

while True:

    try:
        num=int(input("请输入整数"))
        if num>a:
            print("猜大了")
        elif num<a:
            print("猜小了")
        else:
            print("猜对了")
            break
    except ValueError:
        print("输入无效")
'''
a=float(input("请输入一个数"))
b=float(input("请输入一个数"))

sign=input("请输入一个运算符")
if sign=="+":
    print("结果为",a+b)
elif sign=="-":
    print("结果为",a-b)
elif sign=="*":
    print("结果为",a*b)
elif sign=="/":
    if b!=0:
        print("结果为",a/b)
    else:
        print("除数为零！")
else:
    print("输入运算符错误！")


