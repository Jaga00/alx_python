import requests
import sys

def fetch_and_display_response(url):
    """
    Fetches the URL using the requests package, displays the response body,
    and prints an error message if the HTTP status code is greater than or equal to 400.
    """
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
    
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display_response(url)