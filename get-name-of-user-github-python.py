import requests

def get_name(username: str):
    """
    This function takes a GitHub username and outputs the GitHub display name.

    :param username: Any valid GitHub username
    :returns: display name as a string variable.
    """

    API_URL = f"https://api.github.com/users/{username}"
    Response = requests.get(API_URL)
    display_name = str(Response.json()['name'])
    formatted_name_string = f"Name: {display_name}"
    print(formatted_name_string)

    return display_name


def main():
    """
    Demonstrating how to use the get_name() function.
    """

    get_name("asefg482")


if __name__ == "__main__":
    main()
