import requests
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = response1.json()
print(obj["token"])

token = obj["token"]
params = {'token': token}
sleep_time = obj["seconds"]
print(response1.text)

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=params)
obj2 = response2.json()
status = obj2["status"]
assert status == "Job is NOT ready"
time.sleep(sleep_time)
print(response2.text)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=params)
obj3 = response3.json()
status2 = obj3["status"]
assert status2 == "Job is ready"
result=obj3["result"]
print(response3.text)

