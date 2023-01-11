import requests

password = [password, 123456,{'12345678'}, {'qwerty'}, {'abc123'}, {'monkey'}, {'1234567'}, {'letmein'}, {'trustno1'}, {'dragon'}, {'baseball'}, {'111111'}, {'iloveyou'}, {'master'}, {'sunshine'}, {'ashley'}, {'bailey'}, {'passw0rd'}, {'shadow'}, {'123123'}, {'654321'}, {'superman'}, {'qazwsx'}, {'michael'}, {'Football'}]
login = ['super_admin']
params = {"login": login, "password": password}

for i in password:
  for f in login:
   response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=params)
   print(params)
   print(dict(response1.cookies))
   cookie_value = response1.cookies.get('auth_cookie')
   cookies = {'auth_cookie': cookie_value}
   response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
   print(response2.text)
  #if response2.json == "You are authorized":
    #print(response2.text)
   #else:
       #print('неверно')