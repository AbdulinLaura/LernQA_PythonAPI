import requests
url = "https://playground.learnqa.ru/api/homework_cookie"
response = requests.get(url)
body = dict(response.cookies)
print(body)