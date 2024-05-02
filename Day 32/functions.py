import pandas
import smtplib
import random
from datetime import datetime


def get_birthdays() -> list:
    try:
        birthdays = pandas.read_csv("Day 32/birthdays.csv").to_dict(orient="records")
        print(birthdays)
    except Exception as e:
        print(f"Error getting the birthdays: {type(e).__name__}")
    else:
        print("Birthdays saved!")

    return birthdays


def send_email(person: dict, email, password):
    print("name:" + person["name"])

    try:
        with open(f"Day 32/letter_templates/letter_{random.randint(1,3)}.txt") as data_file:
            letter = data_file.read().replace("[NAME]", person["name"])
    except Exception as e:
        print(f"Error getting letter: {type(e).__name__}")
    else:
        print("Letter obtained.")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        try:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}\nHappy {datetime.now().year - person['year']} Years Old."
            )
        except Exception as e:
            print(f"Error sending email: {type(e).__name__}")
        else:
            print(f"Email to {person['name']} sent!")