from webbrowser import get
import requests

endpoint = "http://127.0.0.1:8000/"

get_response = requests.get(endpoint)

get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.status_code)