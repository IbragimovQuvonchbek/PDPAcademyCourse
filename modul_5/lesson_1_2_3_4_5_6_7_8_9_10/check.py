import requests

url = "http://51.20.104.138/api/v1/netflix/api-token-auth/"
data = {
    "username": "ibragimov",
    "password": "ibragimov"
}

response = requests.post(url, data=data)

if response.status_code == 200:
    token = response.json().get("token")
    print("Token:", token)
else:
    print("Failed to obtain token:", response.content)

# 384eed901dd5dbb5d1f259662c9d97cc74a5118a
