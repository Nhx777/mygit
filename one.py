

class restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0
    def open_restaurant(self):
        print(f"{self.name}正在营业")
    def describe_resturant(self):
        print(f"{self.name}餐馆是做{self.type}菜的餐馆")
        print(f"建议大家都来吃这家餐馆")
    def read_restaurant(self):
        print(f"就餐人数为{self.number_served}")
    def set_number_served(self,num):
        self.number_served=num

    def increment_number_served(self,add):
        self.number_served+=add

class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"用户的全名是{self.first_name} {self.last_name}")

class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def get_descriptive_name(self):
        long_name=f'{self.make} {self.model} {self.year}'
        return long_name

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

class elcar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75
    def describe_battery(self):
        print(f"这辆车有{self.battery_size}kwh的大电池")
    def update_battery(self,battery):
        self.battery_size=battery


