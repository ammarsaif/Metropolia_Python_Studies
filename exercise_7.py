# Task 1

seasons = (
    (3,4,5),
    (6,7,8),
    (9,10,11),
    (12,1,2)
)

user_month = int(input('What is the number of month, enter (1-12? '))

spring, summer, autumn, winter = seasons

if user_month in spring:
    print(f"The season for {user_month} is Spring.")
elif user_month in summer:
    print(f"The season for {user_month} is Summer.")
elif user_month in autumn:
    print(f"The season for {user_month} is Autumn.")
elif user_month in winter:
    print(f"The season for {user_month} is Winter.")
else:
    print("Invalid number")


# Task 2

names_list = []


while True:
    user_name = input("Tell me a name ")
    if user_name == "":
        break
    if user_name in names_list:
        print("Existing Name")
    else:
        names_list.append(user_name.lower())
        print("New Name")

print("List of names")
for name in names_list:
    print(name)

# Task 3

airports = {
    'HEL': 'Helsinki'
}

def fetch_airport():
    input_parameter = input("Tell the ICAO code of the airport: ")
    airport_name = airports.get(input_parameter)
    if airport_name is not None:
        print(f"The name of the airport with ICAO code {input_parameter} is {airport_name}.")
    else:
        print(f"Airport with ICAO code {input_parameter} not found.")
def store_airport():
    input_parameter = input("Tell the ICAO code of the airport: ")
    input_value = input("Tell the name of the airport: ")
    airports[input_parameter] = input_value


while True:
    user_input = int(input("Would you like to fetch or store the airport data?\n"
                           "Please press 1 for fetching airport data:\n"
                           "Please press 2 for storing a new airport:\n"
                           "Please press 3 to quit the program: "))

    if user_input == 1:
        fetch_airport()
    elif user_input == 2:
        store_airport()
        print("Airport data stored.")
    elif user_input == 3:
        print("Quitting the program.")
        break

print(airports)
