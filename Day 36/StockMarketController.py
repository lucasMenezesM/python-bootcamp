import requests
from datetime import datetime, timedelta
from dotenv import dotenv_values

config = dotenv_values("Day 36/.env")

STOCK = "TSLA"

class StockMarketController:
    def __init__(self) -> None:
        self.days_data: list = []


    def save_data(self) ->None:
        """COLLECT THE STOCK MARKET DATA FROM LAST DAYS"""

        try:
            response = requests.get(url=config["STOCK_API_ENDPOINT"], params={
                "function": "TIME_SERIES_DAILY",
                "symbol": "TSLA",
                "apikey": config["STOCK_API_KEY"]
            })
            response.raise_for_status()

            data = response.json()["Time Series (Daily)"]
            self.days_data = [value for (key, value) in data.items()]
        except Exception as e:
            print(f"Error saving data from API: {type(e).__name__}")
        else:
            print("Data from stock market collected.")
    

    def get_data(self) -> list:
        """RETURNS A LIST WITH THE DATE OF THE LAST DAYS"""

        if len(self.days_data) == 0:
            raise ValueError("The Stock Market Data Is Empty")
        else:
            return self.days_data


    def get_difference_percentage(self) -> float:
        pass
        # self.save_data()

        # day1_close_value = float(self.get_data()[0]["4. close"])
        # day2_close_value = float(self.get_data()[1]["4. close"])

        # difference = day1_close_value - day2_close_value
        # difference_percentage = (difference / day2_close_value) * 100
        # print("difference: "+difference_percentage)

        # return difference_percentage