import requests
parameters_methods_list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for param in parameters_methods_list:
    response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(
        f"method GET with parameter params={param} has following result {response1} with status code {response1.status_code}")
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"method GET with parameter data={param} has following result {response2} with status code {response2.status_code}")
    response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(
        f"method POST with parameter data={param} has following result {response3} with status code {response3.status_code}")
    response4 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(
        f"method POST with parameter params ={param} has following result {response4} with status code {response4.status_code}")
    response5 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"method PUT with parameter data={param} has following result {response5} with status code {response5.status_code}")
    response6 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(
        f"method PUT with parameter params ={param} has following result {response6} with status code {response6.status_code}")
    response7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(
        f"method DELETE with parameter data={param} has following result {response7} with status code {response7.status_code}")
    response8 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(
        f"method DELETE with parameter params ={param} has following result {response8} with status code {response8.status_code}")
