import requests

url = "http://127.0.0.1:8000/api/v1/netflix/delete-comment/1"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Token 1edd942b74f2872be726576811e89d2cab671bb7"  # Remove the colon after Token
}

response = requests.delete(url, headers=headers)

print("Status Code:", response.status_code)
