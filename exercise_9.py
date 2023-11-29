import random


class Car:
    def __init__(self, reg_num: str, max_speed=150, current_speed=0, total_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.total_distance = total_distance

    def accelerate(self, change_speed):
        min_speed = 0
        new_speed = self.current_speed + change_speed
        self.current_speed = new_speed
        if self.current_speed < self.max_speed:
            if self.current_speed < min_speed:
                self.current_speed = min_speed
            return self.current_speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
            return self.current_speed

    def drive(self, time):
        new_distance = round((self.current_speed * time))
        self.total_distance += new_distance
        return #f"New total distance by adding {time} hrs is {self.total_distance} kms"

    def print_info(self):
        print(f"Name: {self.reg_num} "
              f"Max Speed: {self.max_speed} "
              f"Current Speed: {self.current_speed} "
              f"Mileage: {self.total_distance} ")


car_list = []
car_total = 10
running = True

for x in range(1, car_total + 1):
    random_max_speed = random.randint(100, 200)
    car_list.append(Car(f"ABC-{x}", random_max_speed))


def run_race():
    for car in car_list:
        random_speed = random.randint(-15, 30)
        car.accelerate(random_speed)
        car.drive(1)


def check_mileage():
    for car in car_list:
        if car.total_distance >= 10000:
            print(f"{car.reg_num} has won!!!")
            return False
    return True


while running:
    run_race()
    running = check_mileage()

for car in car_list:
    car.print_info()




