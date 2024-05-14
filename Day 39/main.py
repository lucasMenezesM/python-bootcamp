import requests
from dotenv import dotenv_values
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

config = dotenv_values("Day 39/.env")

data_manager = DataManager()
data_sheet = data_manager.get_all_data()
# # print(data_sheet)

flight_search = FlightSearch()

# flight_search.search_flight(destination_code="LON", origin_code="PAR")
# print(min(price_list))
destinations_result = []

for city in data_sheet:
    flight_list = flight_search.search_flight(origin_code="LON", destination_code=city["iataCode"], maxPrice=city["lowestPrice"])
    price_list = [float(destination["price"]["total"]) for destination in flight_list]
    destinations_result.append({
        "price":{
            "city": city["city"], "lowestPrice": min(price_list), "iataCode": city["iataCode"]
        }
    })

print(destinations_result)

# pprint(flight_list)
# for city in data_sheet:
#     if len(city["iataCode"]) == 0:
#         city["iataCode"] = flight_search.update_iata_code(city_name=city["city"])
#         data_manager.update_spreadsheet(city)