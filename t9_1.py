class restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def open_restaurant(self):
        print(f"{self.name}正在营业")
    def describe_resturant(self):
        print(f"{self.name}餐馆是做{self.type}菜的餐馆")
        print(f"建议大家都来吃这家餐馆")
ndre=restaurant('ning','thai')
dang=restaurant('xiaogou','tomato')
print(ndre.name)

ndre.describe_resturant()
ndre.open_restaurant()
dang.describe_resturant()

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"用户的全名是{self.first_name} {self.last_name}")
ning=User('ning','haixu')
ning.describe_user()

class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def read_odometer(self):
        print(f'这辆车已经{self.odometer}米了')
    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer = mileage
            wodeche.read_odometer()
        else:
            print('别乱调表！')
    def increase(self,mile):
        self.odometer+=mile
wodeche=car('benchi','e300',2020)
wodeche.odometer=100
wodeche.read_odometer()
wodeche.increase(10)
wodeche.read_odometer()
wodeche.update_odometer(200)
wodeche.increase(20)
wodeche.read_odometer()

