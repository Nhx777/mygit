from one import car,elcar

if __name__ == "__main__":
    abc = car('luhu', 'q', 2010)
    print(abc.get_descriptive_name())
    abc.odometer = 24
    abc.read_odometer()
    byd=elcar('byd','qin','2022')
    byd.update_battery(80)
    byd.describe_battery()