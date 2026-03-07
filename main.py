import os
import requests

BASE_URL = "https://app.100daysofpython.dev"
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {"query": input("State your exercise")}

response = requests.post(f"{BASE_URL}/v1/nutrition/natural/exercise", json=data, headers=headers)
print(response.json())