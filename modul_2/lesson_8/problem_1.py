import requests

if __name__ == '__main__':
    url = 'http://iamawesome.com'
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
