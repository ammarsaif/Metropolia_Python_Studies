import random


class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Book name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Author: {self.author} \n"
              f"Total pages: {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Chief Editor: {self.chief_editor}")


book1 = Book("Story Book", "Rosa Liksom", 192)

Donald_Duck = Magazine("Fashion Magazine", "Aki Hyyppä")

book1.print_info()
print()
Donald_Duck.print_info()


# Part 2


class Car:
    def __init__(self, reg_num: str, max_speed=0, total_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.total_distance = total_distance

    def drive(self, time):
        new_distance = round((self.max_speed * time))
        self.total_distance += new_distance
        return f"New total distance by adding {time} hrs is {self.total_distance} kms"

    def print_info(self):
        print(f"Name: {self.reg_num} "
              f"Max Speed: {self.max_speed} "
              f"Total distance covered: {self.total_distance} kms")


class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity, total_distance=0):
        self.battery_capacity = battery_capacity
        super().__init__(reg_num, max_speed, total_distance)

    def print_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        super().print_info()


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, fuel_capacity, total_distance=0):
        self.fuel_capacity = fuel_capacity
        super().__init__(reg_num, max_speed, total_distance)

    def print_info(self):
        print(f"Fuel Capacity: {self.fuel_capacity} litres")
        super().print_info()


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.drive(3)
gasoline_car.drive(3)

print()
electric_car.print_info()
print()
gasoline_car.print_info()
