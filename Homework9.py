import requests
class Test_example:
    def test_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        body = response.headers["x-secret-homework-header"]
        assert "x-secret-homework-header" in response.headers, "There is  no field 'x-secret-homework-header' in the response"
        expected_response_text = "Some secret value"
        actual_response_text = body
        assert expected_response_text == actual_response_text, f"body contains another value {body}"