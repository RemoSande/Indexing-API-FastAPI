# from dotenv import find_dotenv, load_dotenv
# import requests

# load_dotenv(find_dotenv())

# url = "http://localhost:8001/question"
# data = {"question": "Do I need a reservation for Sakura Harmony?"}
# response = requests.post(url, json=data)
# print(response.json())

from dotenv import find_dotenv, load_dotenv
import requests

load_dotenv(find_dotenv())

url = "http://localhost:8001/question"
params = {"question": "Do I need a reservation for Sakura Harmony?"}
response = requests.get(url, params=params)
print(response.json())
