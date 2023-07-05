import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from datetime import datetime
import os

NUTRI_APP_ID = str(os.environ['NUTRI_APP_ID'])
NUTRI_API_KEY = str(os.environ['NUTRI_API_KEY'])
SHEET_ENDPOINT = str(os.environ['SHEET_ENDPOINT'])
ENDPOINT = str(os.environ['ENDPOINT'])
USERNAME = str(os.environ['USERNAME'])
PASSWORD = str(os.environ['PASSWORD'])

print()

# Required HEADERS when accessing Nutritionix V2 API endpoints:
# x-app-id: Your app ID issued from developer.nutritionix.com)
# x-app-key: Your app key issued from developer.nutritionix.com)
# x-remote-user-id:  A unique identifier to represent the end-user who is accessing the Nutritionix API.  If in development mode, set this to 0.  This is used for billing purposes to determine the number of active users your app has.

#user_exercise_sentence = input("What activities did you perform today: ")

query = {
    "query": input("What excercise(s) did you do: "),
    "gender": "male",
    "weight_kg": 92,
    "height_cm": 182.88,
    "age": 18
}

headers = {
    "x-app-id":NUTRI_APP_ID,
    "x-app-key":NUTRI_API_KEY,
    "x-remote-user-id" : '0'
}

excercise_info = requests.post(ENDPOINT, data=query, headers=headers)


# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
current_date = dt_string[0:10]
current_time = dt_string[11:19]

excercise_info = excercise_info.json()
print(excercise_info)

#authentication
basic = HTTPBasicAuth(USERNAME, PASSWORD)
for i in range(0,len(excercise_info["exercises"])):
    query = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": excercise_info["exercises"][i]["user_input"].title(),
            "duration": excercise_info["exercises"][i]["duration_min"],
            "calories": excercise_info["exercises"][i]["nf_calories"]
        }
    }
    spreadsheet_info = requests.post(SHEET_ENDPOINT, json=query, auth=basic)
    print(spreadsheet_info.status_code)



