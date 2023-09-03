import platform
import random
import math


# Task 1

def roll_dice ():
    random_num = random.randint(1, 6)
    return random_num
def main():
    count = 0
    while True:
        result = roll_dice ()
        count += 1
        print(f"roll dice {count}: {result}")
        if roll_dice() == 6:
            break

main = main()
print(main)



# Task 2

def roll_dice (sides):
    random_num = random.randint(1, sides)
    return random_num

def main_sides():
    sides = int(input("What are the maximum side rolls? "))
    count = 0
    max_rolls = sides
    while True:
        result = roll_dice(sides)
        count += 1
        print(f"roll dice {count}: {result}")
        if max_rolls == result:
            break
main_sides = main_sides()
print(main_sides)



# Task 3

def unit_convert (gallons):
    return gallons * 3.78541
def gallons_litres ():
    gallons = int(input("How many gallons you want to convert into litres? "))
    result = unit_convert(gallons)
    print(f"There are {round(result, 2)} litres in {gallons}")

gallons_litres()


# Task 4

def sum_list (numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

numbers_list = [23,5,7,98,24,56]

result = sum_list(numbers_list)

print(f"The sum of the list is, {result}")



# Task 5

def even_list (num_list):
    new_list = []
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

num_list = [3,4,7,44,24,76,58,6]

result = even_list(num_list)

print(result)



def best_value(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius * 2)
    price_sq_meter = (price / area) * 0.0001
    return price_sq_meter

diameter1 = float(input("What is the diameter of pizza # 1? "))
price1 = float(input("What is the price of pizza # 1? "))

diameter2 = float(input("What is the diameter of pizza # 2? "))
price2 = float(input("What is the price of pizza # 2? "))

unit_value1 = best_value(diameter1, price1)
unit_value2 = best_value(diameter2, price2)

if unit_value1 < unit_value2:
    print(f"First pizza offer better value for money")
else:
    print(f"Second pizza offer better value for money")



