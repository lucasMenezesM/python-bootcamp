import requests
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values("Day 37/.env")

API_ENDPOINT="https://pixe.la"

# ? CREATING A USER
# response = requests.post(url=f"{API_ENDPOINT}/v1/users", json={
#     "token": config["USER_TOKEN"],
#     "username": "lucasm",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# })

# response.raise_for_status()

# ? CREATING A GRAPH
# response = requests.post(
#     url=f"{API_ENDPOINT}/v1/users/{config['USERNAME']}/graphs",
#     headers={
#         "X-USER-TOKEN": config["USER_TOKEN"]
#     },
#     json={
#         "id": "graph1",
#         "name": "Programming days",
#         "type": "float",
#         "unit": "hours",
#         "color": "ajisai"
#     }
# )

# print(response.json())

# ? POSTING A PIXEL INTO THE GRAPH

today = datetime.now()

# response = {}
# while response["message"] != "Success":

#     response = requests.post(
#         url=f"{API_ENDPOINT}/v1/users/{config['USERNAME']}/graphs/graph1",
#         headers={
#             "X-USER-TOKEN": config["USER_TOKEN"]
#         },
#         json={
#             "date": today.strftime("%Y%m%d"),
#             "quantity": "3.2",
#         }
#     )

# print(response.json())

# ? UPDATING A PIXEL

response = requests.put(
    url=f"{API_ENDPOINT}/v1/users/{config['USERNAME']}/graphs/graph1/{today.strftime('%Y%m%d')}",
    headers={
        "X-USER-TOKEN": config["USER_TOKEN"]
    },
    json={
        "quantity": "4.7",
    }
)

print(response.json())