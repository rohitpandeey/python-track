# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def full_name(self):
#         return f"{self.brand} {self.model}"

        
#self is same as this here

# my_car=Car()
# print(my_car)
# # \<__main__.Car object at 0x102208af0>

# my_car=Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_car=Car("Tata","Safari")



#Inheritance

# class ElectricCar(Car):

#     def __init__(self,brand,model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size= battery_size


# my_tesla= ElectricCar("Tesla","Model X", "85kWh")
# print(my_tesla.model)
# print(my_tesla.full_name())



# # Encapsulation in Python

# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.model=model

#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.brand} {self.model}"


# class ElectricCar(Car):

#     def __init__(self,brand,model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size= battery_size


# my_tesla= ElectricCar("Tesla","Model X", "85kWh")

# # print(my_tesla.brand)
# print(my_tesla.get_brand())



# #Polymorphism


# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.model=model

#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def fuel_type(self):
#         return "petrol or diesel"

# class ElectricCar(Car):

#     def __init__(self,brand,model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size= battery_size

#     def fuel_type(self):
#         return "Electric Charge"


# my_tesla= ElectricCar("Tesla","Model X", "85kWh")
# print(my_tesla.fuel_type())


# safari= Car("tata","Safari")
# print(safari.fuel_type())


#Class Variable
class Car:
    total_car=0

    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        # self.total_car+=1
        Car.total_car+=1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    
    def fuel_type(self):
        return "petrol or diesel"
    
    #static method
    @staticmethod
    def general_desc():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):

    def __init__(self,brand,model, battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla= ElectricCar("Tesla","Model X", "85kWh")

# isinstance()
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

print(my_tesla.fuel_type())


# safari= Car("tata","Safari")
# print(safari.fuel_type())
# print(safari.total_car)

# test=Car("test","test")
# print(test.total_car)

# print(Car.total_car)
# safari.model="city"
# print(safari.model)

#Static Methods

# print(safari.general_desc())
# print(Car.general_desc())


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla= ElectricCarTwo("tesla","model-s")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())