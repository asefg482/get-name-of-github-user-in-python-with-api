import requests

class User_Finder:
    
    def __init__(self, username):
        self.username = username

    @property
    def display_name():
        """
        Takes a GitHub username and outputs the GitHub display name.

        :param username: Any valid GitHub username
        :returns: display name as a string variable.
        """

        API_URL = f"https://api.github.com/users/{self.username}"
        response = requests.get(API_URL)
        display_name = str(response.json()['name'])
        formatted_name_string = f"Name: {display_name}"
        print(formatted_name_string)

        return display_name
