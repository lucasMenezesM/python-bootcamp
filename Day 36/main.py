from dotenv import dotenv_values
from NewsList import NewsList
from StockMarketController import StockMarketController
import smtplib

config = dotenv_values("Day 36/.env")

STOCK = "TSLA"
COMPANY_NAME = "Facebook"

stock_market = StockMarketController()
stock_market.save_data()
stock_market_data_list = stock_market.get_data()
# print(stock_market.get_data())

day1_close_value = float(stock_market_data_list[0]["4. close"])
day2_close_value = float(stock_market_data_list[1]["4. close"])

difference = day1_close_value - day2_close_value
difference_percentage = (difference / day2_close_value) * 100
print(difference_percentage)

news_list = NewsList()
news_list.save_news(quantity=3)
news = news_list.get_news()
print("\n\n\nNews collected:\n")

def send_email():
    if not news:
        return
    
    if day1_close_value == day2_close_value:
        return
    
    email_title: str
    if day1_close_value > day2_close_value:
        email_title = f"{STOCK} 🔺{round(difference_percentage,2)}%".encode("ascii", "ignore")
    elif day2_close_value > day1_close_value:
        email_title = f"{STOCK} 🔻{round(difference_percentage,2)}%".encode("ascii", "ignore")

    email_body: str = ""

    for index, article in enumerate(range(len(news))):
        email_body += f"{news[index].title}\n{news[index].description}\n\nBy: {news[index].source_name} - {news[index].author}\n\n"

    print(f"{email_title}\n\n{email_body}")

    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config["FROM_EMAIL"], password=config["APP_PASSWORD"])

            connection.sendmail(
                from_addr=config["FROM_EMAIL"],
                to_addrs=config["TO_EMAIL"],

                msg=f"Subject:{email_title}\n\n{email_body}"
            )
    except Exception as e:
        print(f"Error sending email: {type(e).__name__}")
    else:
        print("Email Sent")
    
send_email()


# news_list.save_news(quantity=2)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

