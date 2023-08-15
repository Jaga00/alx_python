import requests
import sys

def get_user_id(username, access_token):
    """
    Fetches the user ID using the GitHub API and a personal access token.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        return user_id
    else:
        print("Error: Unable to fetch user ID. Status code:", response.status_code)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <username> <access_token>")
    else:
        username = sys.argv[1]
        access_token = sys.argv[2]
        user_id = get_user_id(username, access_token)
        
        if user_id is not None:
            print("User ID:", user_id)