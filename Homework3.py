import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response2.text)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response3.text)


response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"})
print(response3.text)







