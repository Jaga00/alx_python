import requests
import sys

def fetch_and_display_request_id(url):
    """
    Fetches the URL using the requests package, retrieves the value of the X-Request-Id
    variable from the response header, and displays it.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
    else:
        print("Error: Unable to fetch URL. Status code: {}".format(response.status_code))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
    else:
        url = sys.argv[1]
        fetch_and_display_request_id(url)