from datetime import datetime
import requests
from dotenv import dotenv_values

config = dotenv_values("Day 38/.env")

class Spreadsheet:
    def __init__(self) -> None:
        pass


    def update_spreadsheet(self, exercises_list: list) -> None:

        now = datetime.now()
        current_time = str(now.time()).split(".")[0]

        for exercise in exercises_list:
            response = requests.post(
                url=config["sheety_api_endpoint"],
                headers={"Authorization": f"Bearer {config['spreed_sheet_token']}"},
                json={
                    "workout": {
                        "date": str(now.strftime("%d/%m/%Y")),
                        "time": current_time,
                        "exercise": exercise["name"],
                        "duration": exercise["duration_min"],
                        "calories": exercise["nf_calories"]
                    }
                }
            )
