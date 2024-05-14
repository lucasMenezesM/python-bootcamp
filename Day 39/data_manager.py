#This class is responsible for talking to the Google Sheet.
from dotenv import dotenv_values
import requests
from pprint import pprint

config = dotenv_values("Day 39/.env")
headers = {"Authorization": f'Bearer {config["sheety_token"]}'}

class DataManager:
    def __init__(self) -> None:
        self.sheet_data = []
    
    def update_spreadsheet(self, place: dict):
        response = requests.put(
            url=f'{config["sheety_api_endpoint"]}/{place["id"]}',
            headers=headers,
            json={
                "price": {
                    "city": place["city"],
                    "iataCode": place["iataCode"],
                    "lowestPrice": place["lowestPrice"]
                }
            }
        )

        print(response.json())

    
    def get_all_data(self):
        
        response = requests.get(
            url=config["sheety_api_endpoint"],
            headers=headers,
        )

        # return self.sheet_data
        # print(response.json())
        return response.json()["prices"]