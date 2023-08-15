import requests
import sys

def send_post_request_and_display_response(url, email):
    """
    Sends a POST request to the provided URL with the email as a parameter
    and displays the body of the response.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print("Error: Unable to fetch URL. Status code: {}".format(response.status_code))

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request_and_display_response(url, email)
