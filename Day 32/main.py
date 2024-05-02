# import smtplib


my_email = ""
to_email = ""
my_password = ""
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="First Email Sent"
#     )




# current_date = dt.datetime.now()
# current_day = current_date.weekday()
# print(current_day)

# with open("Day 32/quotes.txt", mode="r", encoding="utf-8") as data_file:
#     data = data_file.readlines()
#     quote = random.choice(data).strip().encode("ascii", "ignore")
#     print(quote)

# if current_day == 2:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)

#         try:
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=to_email,
#                 msg=f"Subject:Good Monday! \n\nHello! Good Monday!\n{quote}"
#             )
#         except Exception as e:
#             print(f"Error sending email: {type(e).__name__}")
#         else:
#             print("Email Sent")


##################### BirthDay Wisher Project ######################

import datetime as dt
from functions import get_birthdays, send_email

current_date = dt.datetime.now()
day = current_date.day
month = current_date.month

birthdays_list = get_birthdays()

birthday_people = [person for person in birthdays_list if person["month"] == month and person["day"] == day]

if birthday_people:
    for person in birthday_people:
        send_email(person, email=my_email, password=my_password)
else:
    print("no one has a birthday today")

