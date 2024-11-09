import requests
url = "https://jsonplaceholder.typicode.com/invalid-url"

try:
    response = requests.get(url)

    response.raise_for_status()
    
    print(response.json())

except requests.exceptions.HTTPError as httperr:
    print(f"Error: {httperr}")

except requests.exceptions.RequestException as reqerr:
    print(f"Error: {reqerr}")

except Exception as e:
    print(f"Error: {e}")