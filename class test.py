class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} 在舔我的脚")

    def rolling(self):
        print(f"{self.name} 在sword new new")
my_dog=Dog('DZH',20)
print(f"我的小狗的名字是{my_dog.name}")
print(f"她的年龄是{my_dog.age}岁")
print(my_dog.name)
my_dog.sit()
my_dog.rolling()

DaHuang=Dog('Dahuang',6)
DaHuang.sit()
DaHuang.rolling()

