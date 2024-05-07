import requests
import smtplib
import os
from dotenv import load_dotenv, dotenv_values

# load_dotenv()
config = dotenv_values("Day 35 - Rain Alert/.env")

api_url = config["api_url"]
five_days_forecast_url = config["five_days_forecast_url"]
api_key = config["api_key"]
MY_LAT = config["MY_LAT"]
MY_LNG = config["MY_LNG"]
MY_EMAIL = config["MY_EMAIL"]
TO_ADDRS = config["TO_ADDRS"]
APP_PASSWORD = config["APP_PASSWORD"]

# print(config)


# 5 day forecast with a 3-hour step
# api.openweathermap.org/data/2.5/forecast?lat=-21.754530&lon-41.324612=&appid=

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=-21.754530&lon=-41.324612&appid="")
params = {
    "lat": -1.371860,
    "lon": -48.429700,
    "appid": api_key,
    "cnt": 4
}
# response = requests.get(url=f"{five_days_forecast_url}?lat={MY_LAT}&lon={MY_LNG}&appid={api_key}")
response = requests.get(url=five_days_forecast_url, params=params)

response.raise_for_status()
data = response.json()
weather_id = data["list"][0]["weather"][0]["id"]
weather_description = data["list"][0]["weather"][0]["description"]
weather_list = data["list"]
# print(weather_list)

will_raining = False

for weather in weather_list:
    id = weather["weather"][0]["id"]
    print(id)
    will_raining = True

if will_raining:
    with smtplib.SMTP("smtpm.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)

        connection.sendmail(
            to_addrs=TO_ADDRS,
            from_addr=MY_EMAIL,
            msg=f"Subject:Hey, look up!\n\n"
        )
