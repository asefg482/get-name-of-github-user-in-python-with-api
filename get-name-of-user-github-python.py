import requests

def getUsername(user):
    username = "";
    API_URL=f"https://api.github.com/users/{user}"
    Response = requests.get(API_URL)
    if Response.status_code == 200:
        username = Response.json()['name']
    else:
        username = "User Not Found"
    return username

def main():
    username = getUsername("asefg482")
    print(f"Name : {username}")

main()