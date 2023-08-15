import requests
import sys

def search_user_with_letter(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter,
    and displays the id and name from the JSON response or appropriate messages.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    
    response = requests.post(url, data=payload)
    
    try:
        json_response = response.json()
        
        if json_response:
            user_id = json_response.get('id')
            user_name = json_response.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    
    search_user_with_letter(letter)