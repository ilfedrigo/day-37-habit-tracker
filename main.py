import requests
from datetime import datetime

USERNAME = "ilfedrigo"
TOKEN = "ilfedrigo"
GRAPH_ID = "graph1"

today = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "days",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# response = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", headers=headers, json=pixel_data)

print(response.text)