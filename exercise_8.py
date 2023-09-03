import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1472',
    autocommit=True
)


# Task 1

def airport_name(input):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"

    cursor = connection.cursor()
    cursor.execute(sql, (input,))
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport Name: {row[0]}")
            print(f"Location: {row[1]}")
    else:
        print("Airport not found for the given ICAO code.")

user_icao = input("Tell the ICAO code of the airport: ")
airport_name(user_icao)


# Task 2

def airport_name(input):
    sql = "SELECT name, type FROM airport WHERE iso_country = %s order by type"

    cursor = connection.cursor()
    cursor.execute(sql, (input,))
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        count = 0
        for row in result:
            count += 1
            print(f"Airport {count} - Name: {row[0]}, Type: {row[1]}")
        print(count)
    else:
        print("Airport not found for the given ICAO code.")

user_input = input("Tell the country code of the airport: ")
airport_name(user_input)

#Task 3

def get_airport_coordinates(icao_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

    cursor = connection.cursor()
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    latitude, longitude = result
    return latitude, longitude


def calculate_distance(icao_code1, icao_code2):
    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    distance = geodesic(coordinates1, coordinates2).kilometers
    return distance

icao_code1 = input("Enter the ICAO code of the first airport: ")
icao_code2 = input("Enter the ICAO code of the second airport: ")

distance = calculate_distance(icao_code1, icao_code2)

if distance is not None:
    print(f"Distance between airports {icao_code1} and {icao_code2}: {distance:.2f} kilometers")
else:
    print("One or both airports not found.")





