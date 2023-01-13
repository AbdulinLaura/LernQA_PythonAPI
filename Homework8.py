import requests
class Test_example:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        body = response.cookies["HomeWork"]
        assert response.status_code == 200, "Wrong response code"
        assert "HomeWork" in response.cookies, "There is  no field 'HomeWork' in the response"
        expected_response_text = "hw_value"
        actual_response_text = body
        assert expected_response_text == actual_response_text, f"body contains another value {body}"



