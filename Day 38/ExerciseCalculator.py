import requests
from dotenv import dotenv_values

config = dotenv_values("Day 38/.env")
headers = {
    'Content-Type': 'application/json',
    'x-app-id': config["api_id"],
    'x-app-key': config["api_key"]
}

class ExerciseCalculator:
    def __init__(self) -> None:
        self.exercies_list = []


    def calculate_exercises(self, weight: float, height: float, age: int) -> list:
        response = requests.post(
            url= f"{config["nutritionix_api_endpoint"]}/natural/exercise",
            headers=headers,
            json={
                "query": input("What exercise did you do?"),
                "weight_kg": weight,
                "height_cm": height,
                "age": age
            }
        )
        
        self.exercies_list = response.json()["exercises"]
        return self.exercies_list
    

    def get_nutrient_breakdown():

        response = requests.post(
            url= f"{config["nutritionix_api_endpoint"]}/natural/nutrients",
            headers=headers,
            json={
                "query": input("Type a food name: "),
            }
        )
        return response.json()
