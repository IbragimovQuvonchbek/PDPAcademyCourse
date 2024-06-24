import requests

url_add = "http://127.0.0.1:8000/api/v1/netflix/movies/add-actor/?movie_id=2&actor_id=1"
url_remove = "http://127.0.0.1:8000/api/v1/netflix/movies/remove-actor/?movie_id=2&actor_id=1"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Token 1edd942b74f2872be726576811e89d2cab671bb7"  # Remove the colon after Token
}

response_add = requests.post(url_add, headers=headers)
response_remove = requests.delete(url_remove, headers=headers)

print("Status Code:", response_add.status_code)
print(response_add.text)

print("Status Code:", response_remove.status_code)
print(response_remove.text)
