import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "reading",
#     "unit": "pages",
#     "type": "int",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date": TODAY,
    "quantity": input("How many pages did you read today? ")
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{TODAY}"

response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)

# response = requests.delete(url=pixel_endpoint, headers=headers)

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
#
print(response.text)
