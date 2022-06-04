import requests
import time

api_baseurl = "https://api.github.com/users"


class User:
    def __init__(self, username):
        self.username = username
        self.response = requests.get(f"{api_baseurl}/{username}")
        self.user_data = self.response.json()


    def getName(self) -> str:
        if self.user_data["name"] == "null":
            return "Hidden/Not Specified"

        return self.user_data["name"]

    def is_valid(self) -> bool:
        try:
            if self.response.json()["message"] == "Not Found":
                print(f"{self.username} not found.")
                return False

            return True
        except KeyError as e:
            if e.args[0] == "message":
                return True

            return False


def main():
    print("GET GITHUB USER INFORMATION")
    login = str(input("Username: "))
    if login != "" or login is not None:
        get_all_user_information(login)
    else:
        print("Username cannot be empty.")
        time.sleep(1)
        main()


def get_all_user_information(username):

    user = User(username)

    if not user.is_valid():
        print(f"No username {username} found in Github API.")
        time.sleep(2)
        main()
        return

    print(f"Name: {user.getName() if not user.getName() is None else 'Hidden/Unspecified'}")


if __name__ == "__main__":
    main()
