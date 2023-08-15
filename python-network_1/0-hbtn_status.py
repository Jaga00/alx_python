import requests

def fetch_and_display_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status using the requests package
    and displays the response body with tabulation.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    else:
        print("Error: Unable to fetch status. Status code: {}".format(response.status_code))

if __name__ == "__main__":
    fetch_and_display_status()