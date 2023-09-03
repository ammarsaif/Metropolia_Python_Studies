import math
import random

# Task 1 Printing username

userName = input("What is your first name?")
print("Welcome", userName)

# Task 2 Printing username

inputRadius = int(input("Please type the radius of circle?"))
pi = math.pi
areaCircle = pi*inputRadius**2
print("Area of the circle is ", round(areaCircle, 2))

# Task 3 Area and perimeter of rectangle

length = int(input("please provide length"))
width = int(input("please provide width"))
area = length * width
perimeter = 2 * (length * width)
print("Area of rectangle is", area, ", and the perimeter of rectangle is", perimeter)

# Task 4 sum, product, and average of numbers

firstNumber = int(input("please provide first number"))
secondNumber = int(input("please provide second number"))
thirdNumber = int(input("please provide third number"))

sumNumbers = firstNumber + secondNumber + thirdNumber
productNumbers = firstNumber * secondNumber * thirdNumber
averageNumbers = round((firstNumber + secondNumber + thirdNumber) / 3, 3)

print("sum of given numbers is", sumNumbers)
print("product of given numbers is", productNumbers)
print("average of given numbers is", averageNumbers)

# task 5 Medieval weight units

talentsInput = int(input("please provide talents "))
poundsInput = int(input("please provide pounds "))
lotsInput = int(input("please provide lots "))

talentsConversion = talentsInput * 20 * 0.453
poundsConversion = poundsInput * 0.453
lotsConversion = lotsInput * 0.03307 * 0.453
totalWeight = talentsConversion + poundsConversion + lotsConversion
grams = round(totalWeight % 1, 3) * 1000

print(grams)

print("Total Weight is ", math.trunc(totalWeight), "kgs and ", math.trunc(grams), "grams")

# Task 6

thousand = random.randint(1, 6)
hundred = random.randint(1, 6)
tens = random.randint(1, 6)
ones = random.randint(1, 6)
randomThreeCode = random.randint(100, 999)

print(randomThreeCode)
print((thousand * 1000) + (hundred * 100) + (tens * 10) + ones)
