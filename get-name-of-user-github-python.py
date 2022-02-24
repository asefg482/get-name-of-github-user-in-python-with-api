import requests
API_URL="https://api.github.com/users/asefg482"
Response = requests.get(API_URL)
print("Name : "+Response.json()['name'])