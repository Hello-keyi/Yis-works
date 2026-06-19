import pytest
import Class

@pytest.fixture
def car ():
    my_car = Class.Car("audi","a4",2024)
    return my_car

def test_get_descriptive_name(self):
        long_name =( f"{self.make},"
        f"{self.model},"
        f"{self.year}"
        )
        return long_name

def test_read_odometer(self):
        print("this car has "
            f"{self.odometer_reading} mile on it.")
        
def test_update_odometer(self,mileage):
        if self.odometer_reading <= mileage :
            self.odometer_reading = mileage
        else:
            print("you can't roll back this odometer.")

def test_increnent(self,miles):
        self.odometer_reading += miles