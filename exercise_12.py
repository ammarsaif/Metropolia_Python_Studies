import requests
import json

# Task 1

joke_request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(joke_request)
    if response.status_code == 200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

# Task 2

user_location = input("Enter your location: ").capitalize()

weather_request = f"https://api.weatherapi.com/v1/current.json?key=af0d712befef4955832120333232911&q={user_location}&aqi=no"
try:
    response = requests.get(weather_request)
    if response.status_code == 200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        print(json_response["current"]['temp_c'], "degrees celsius")
        print("Current condition:", json_response["current"]['condition']["text"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
