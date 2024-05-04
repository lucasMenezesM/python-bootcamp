from tkinter import *
import requests
from datetime import datetime
import smtplib


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     if response.status_code == 200:
#         quote = response.json()["quote"]
#         canvas.itemconfig(quote_text, text=quote)
#         print(quote)
#     else:
#         response.raise_for_status()
#     #Write your code here.



# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="Day 33/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="Day 33/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()

SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"
NOTIFY_API_URL = "http://api.open-notify.org/iss-now.json"
MY_LAT = None
MY_LNG = None
MY_EMAIL = ""
MY_PASSWORD = ""

current_date = datetime.now()

def is_overhead():
    response = requests.get(url=NOTIFY_API_URL)
    response.raise_for_status()
    data = response.json()

    iss_coordinates = {
        "lat": float(data["iss_position"]["longitude"]),
        "lng": float(data["iss_position"]["latitude"])
    }

    print(iss_coordinates)
    return MY_LAT-5 <= iss_coordinates["lat"] <= MY_LAT+5 and MY_LNG-5 <= iss_coordinates["lng"] <= MY_LNG+5


def is_night():
    response = requests.get(url=SUNRISE_SUNSET_API_URL+f"?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
    response.raise_for_status()

    data = response.json()["results"]

    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    current_hour = current_date.hour

    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")
    print(f"Current Hour: {current_hour}")

    return sunset <= current_hour <= sunrise


if is_night() and is_overhead():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        try:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="",
                msg="Subject:Look UP!\n\nJust look up"
            )
        except Exception as e:
            print(f"Error sending email: {type(e).__name__}")
        else:
            print("Email Sent.")