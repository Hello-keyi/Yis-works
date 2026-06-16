class dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def sit (self):
        print(f"{self.name} is now sitting.")

    def roll_over (self):
        print(f"{self.name} rolled over.")

#--------------------------------------------------------------------------------------------

my_dog = dog("meitan",2)
print(f"name is {my_dog.name}.")
print(f"age is {my_dog.name}.")
my_dog.sit()
my_dog.roll_over()

your_dog = dog("wangcai",1)
your_dog.sit()
your_dog.roll_over()

#---------------------------------------------------------------------------------------------

class Car :

    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name =( f"{self.make},"
        f"{self.model},"
        f"{self.year}"
        )
        return long_name
    
    def read_odometer(self):
        print("this car has "
            f"{self.odometer_reading} mile on it.")
        
    def update_odometer(self,mileage):
        if self.odometer_reading <= mileage :
            self.odometer_reading = mileage
        else:
            print("you can't roll back this odometer.")

    def increnent(self,miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"the car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        print("this car don't have gas tank.")

#-------------------------------------------------------------------------------------

my_car = Car("audi","a4",2024)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.odometer_reading = 3
my_car.read_odometer()
my_car.update_odometer(23)
my_car.read_odometer()
my_car.update_odometer(2)
my_car.read_odometer()
my_car.increnent(3)
my_car.read_odometer()


my_leaf = ElectricCar("nissan","leaf",2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

