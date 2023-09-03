import random
import math

# Task 1

i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

# Task 2

user_input = float(input("How many inches to be converted into centimeters?"))
cm_conversion = float(user_input * 2.54)
while user_input:
    if user_input > 0:
        print(f"There are {cm_conversion} in these {user_input}")
        break
    else:
        print("invalid value")
        break


# Task 3

highest_number = None
lowest_number = None
while True:
    user_input = input("Tell me a number")
    if user_input == "":
        break
    if user_input:
        number = int(user_input)
        if highest_number is None or number > highest_number:
            highest_number = number
        if lowest_number is None or number < lowest_number:
            lowest_number = number

print(f"Highest number is {highest_number}")
print(f"lowest number is {lowest_number}")

#Task 4

random_number = random.randint(1,10)
while True:
    guess_number = int(input("Guess a number!!!"))
    if guess_number == random_number:
        print("Correct guess!")
        break
    elif guess_number < random_number:
        print("Too Low!!!")
    else:
        print("Too high!!!")

# Task 5

username = "python"
password = "rules"
count = 0

while True:
    input_name = input("Type your username!")
    input_password = input("Type your password!")
    if input_name == username and input_password == password:
        print(f"Welcome {username}!!!")
        break
    if input_name != username or input_password != password:
        count += 1
    if count == 5:
        print("access denied")
        break
# Task 6



