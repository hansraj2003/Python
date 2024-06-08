class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    # def get_brand(self):
    #     return self.__brand + " !"
    def chai_brand(self):
        return self.__brand + " !"

    def full_Name(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():                                     #self is not required while using static method
        return "Cars"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"


# my_car = Car("Mahindra", "Thar")
# print(my_car.fuel_type())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_Name())

# car2 = Car("Tata", "Safari")
# car2.model = "Nexon"
# print(car2.total_car)
# print(car2.brand)
# print(car2.model)
# print(car2.full_Name())

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.model)
# print(my_tesla.brand)
# print(my_tesla.chai_brand())
# print(my_tesla.battery_size)
# print(my_tesla.fuel_type())
# print(my_tesla.full_Name())
# print(my_tesla.total_car)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(Car.total_car)
# print(my_car.general_description())
# print(Car.general_description())

class Battery:
    def battery_info(self):
        return "This is battery!"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
