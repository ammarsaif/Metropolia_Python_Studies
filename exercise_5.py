import math
import random

# Task 1

dice_num = int(input("How many dices to roll?"))
count = 0
for num in range(dice_num):
    random_num = random.randint(1, 6)
    count = count + random_num
print(count)

# Task 2


list = []
while True:
    input_num = input("Tell me a number!")
    if input_num == "":
        print("exited")
        break
    number = int(input_num)
    list.append(number)
    sort_list = list.sort(reverse=True)

print(list[0:5])


# Task 3

input_number = int(input("Tell me a number to check for prime number!"))

if input_number <= 1:
    print(f"{input_number} is not a prime number")
else:
    for num in range(2 , input_number):
        if (input_number % num) == 0:
            print(f"{input_number} is not a prime number")
            break
    else:
        print(f"{input_number} is a prime number")

# Task 4
cities = []
count = 0

for i in range(5):
    city_name = input("Tell me the name of a city: ")
    cities.append(city_name)
for city in cities:
    print(city)