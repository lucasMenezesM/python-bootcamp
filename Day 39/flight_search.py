#This class is responsible for talking to the Flight Search API.
import requests
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values("Day 39/.env")
flight_api_endpoint = "https://test.api.amadeus.com/v1"

headers = {"Authorization": f'Bearer {config["flight_api_token"]}'}

class FlightSearch:    

    def get_token(self):
        data = {
        "grant_type": "client_credentials",
        "client_id": config["flight_api_key"],
        "client_secret": config["api_secret"]
        }

        formatted_data = '&'.join([f"{key}={value}" for key, value in data.items()])

        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=formatted_data 
        )

        print(response.json())

    def update_iata_code(self, city_name):
        # code = "TESTING"

        response = requests.get(
            url=f"{flight_api_endpoint}/reference-data/locations/cities",
            headers=headers,
            params={
                "keyword": city_name
            }
        )

        code = response.json()["data"][0]["iataCode"]
        return code
    

    def search_flight(self, destination_code: str, origin_code: str, maxPrice: int) -> list:

        today = datetime.now().strftime("%Y-%m-%d")
        
        response = requests.get(
            url=f"https://test.api.amadeus.com/v2/shopping/flight-offers?",
            headers=headers,
            params={
                "originLocationCode": origin_code,
                "destinationLocationCode": destination_code,
                "departureDate": today,
                "adults": "1",
                # "maxPrice": maxPrice
            }
        )

        response.raise_for_status()
        # print(response.json()["data"])

        if response.status_code == 200:
            # if len(response.json()["data"]) == 0:
            #     return 0
            # else:
            return response.json()["data"]
        else:
            return