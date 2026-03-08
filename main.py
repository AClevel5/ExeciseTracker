import os
import requests
from datetime import datetime

BASE_URL = "https://app.100daysofpython.dev"
SHEETY_URL = "https://api.sheety.co/14f7d1cbe8332fa058d95bac9f80e54f/workoutTracker/sheet1"
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")


headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {"query": input("State your exercise")}

response = requests.post(f"{BASE_URL}/v1/nutrition/natural/exercise", json=data, headers=headers)
data_list = list(response.json()["exercises"])


today = datetime.now().strftime("%Y-%m-%d")
today_time = datetime.now().strftime("%H:%M:%S")

sheet_data_to_add = {
    "sheet1":{
        "date": today,
        "time": today_time,
        "exercise": data_list[0]["name"],
        "duration": data_list[0]["duration_min"],
        "calories": data_list[0]["nf_calories"],
    }
}


# sheet_response = requests.get("https://api.sheety.co/14f7d1cbe8332fa058d95bac9f80e54f/workoutTracker/sheet1")
# print(sheet_response.json())
sheet_response = requests.post(url=SHEETY_URL, json=sheet_data_to_add)
print(sheet_response.text)
