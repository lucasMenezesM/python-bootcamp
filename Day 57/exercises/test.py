import requests

response = requests.get(f"https://api.genderize.io/?name=lucas")
response.raise_for_status()
data = response.json()
print(data)
# print(data["name"])
print("data type:")
print(type(data))