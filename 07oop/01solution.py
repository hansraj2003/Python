class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    # def get_brand(self):
    #     return self.__brand + " !"
    def chai_brand(self):
        return self.__brand + " !"

    def full_Name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# my_car = Car("Mahindra", "Thar")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_Name())

# car2 = Car("Tata", "Safari")
# print(car2.brand)
# print(car2.model)
# print(car2.full_Name())

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
# print(my_tesla.brand)
print(my_tesla.chai_brand())
print(my_tesla.battery_size)
# print(my_tesla.full_Name())