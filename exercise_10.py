import random


class Elevator:
    def __init__(self, top_floor, current_floor=int, bottom_floor=0):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor

    def go_to_floor(self, floor):
        if self.bottom_floor <= floor <= self.top_floor:
            self.current_floor = floor
            print(f"Elevator is now at floor", self.current_floor)
        else:
            print("Invalid input")

    def floor_up(self, floors):
        next_input = self.current_floor + floors
        if next_input <= self.top_floor:
            self.current_floor = next_input
            print("Current floor is", self.current_floor)
        else:
            print("Invalid input")
        return

    def floor_down(self, floors):
        next_input = self.current_floor - floors
        if next_input >= self.bottom_floor:
            self.current_floor = next_input
            print("Current floor is", self.current_floor)
        else:
            print("Invalid input")
        return


class Building:
    def __init__(self, top_floor, bottom_floor, num_elevators, selected_elevator=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.num_elevators = num_elevators
        self.selected_elevator = selected_elevator
        self.elevator = [Elevator(top_floor=top_floor) for _ in range(num_elevators)]

    def run_elevator(self, selected_elevator, destination_floor):
        if (selected_elevator > 0) and (selected_elevator <= self.num_elevators):
            elevator = self.elevator[selected_elevator - 1]
            elevator.go_to_floor(destination_floor)
        else:
            print("Invalid input!!")
        return

    def fire_alarm(self):
        for elevator in self.elevator:
            elevator.go_to_floor(self.bottom_floor)


def main():
    building_1 = Building(top_floor=15, bottom_floor=0, num_elevators=2)
    building_1.run_elevator(selected_elevator=1, destination_floor=8)
    building_1.run_elevator(selected_elevator=2, destination_floor=5)
    building_1.fire_alarm()


if __name__ == "__main__":
    main()


# Part 2
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
        return  # f"New total distance by adding {time} hrs is {self.total_distance} kms"

    def print_info(self):
        print(f"Name: {self.reg_num} "
              f"Max Speed: {self.max_speed} "
              f"Current Speed: {self.current_speed} "
              f"Mileage: {self.total_distance} ")


class Race:
    def __init__(self, name, distance_km, list_cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = list_cars

    def hour_pass(self, time):
        for race_car in self.cars:
            random_speed = random.randint(-15, 30)
            race_car.accelerate(random_speed)
            race_car.drive(time)

    def print_info(self):
        print(f"Race Name: {self.name}\n"
              f"Race Distance: {self.distance_km} ")

    def check_mileage(self, race_distance):
        for race_car in self.cars:
            if race_car.total_distance >= race_distance:
                print(f"Player: {race_car.reg_num} with mileage: {race_car.total_distance} km has WON!!")
                return False
        return True


car_total = 10
race_distance = 8000

car_list = [Car(f"ABC-{x}", random.randint(100, 200)) for x in range(1, car_total + 1)]
new_race = Race("Derby", race_distance, car_list)

running = True

print()
new_race.print_info()
print()
while running:
    new_race.hour_pass(1)
    running = new_race.check_mileage(race_distance)

print()

for car in car_list:
    car.print_info()
