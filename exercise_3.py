# Task 1

zanderLength = int(input("What is the length of zander?"))
minLength = 42
lengthDiff = -(zanderLength - minLength)

if zanderLength < minLength:
    print("This zander is", lengthDiff, "cm short from the required length. Please throw it back to the lake")
else:
    print("This zander is okay")

# Task 4

cabinClass = input("Which class of cruise ship ticket do you have?")

if cabinClass == "LUX":
    print("LUX: upper-deck cabin with a balcony")
elif cabinClass == "A":
    print("A: above the car deck, equipped with a window")
elif cabinClass == "B":
    print("B: windowless cabin above the car deck")
elif cabinClass == "C":
    print("C: windowless cabin below the car deck")
else:
    print("Invalid cabin class")


# Task 3

gender = input("What is your gender?")
hemoglobin = int(input("What is your hemoglobin?"))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin > 117 & hemoglobin < 155:
        print("Your hemoglobin level is fine.")
    else:
        print("Your hemoglobin is high.")
if gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin > 134 & hemoglobin < 167:
        print("Your hemoglobin level is fine.")
    else:
        print("Your hemoglobin is high.")

# Task 5

year = int(input("What is the year?"))

if year < 99:
    if year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    if year % 100 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
