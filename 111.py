import requests



parameters_methods = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]


for param in parameters_methods:
                response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
                response1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
                response2 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
                response3 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
                print(i, param, response.text)
                print(i, param, response1.text)
                print(i, param, response2.text)
                print(i, param, response3.text)