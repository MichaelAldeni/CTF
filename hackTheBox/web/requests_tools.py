import requests

url = 'http://web-11.challs.olicyber.it/login'

payload = {'username': 'admin', 'password': 'admin'}
headers = {'accept': 'application/json'}
cookies = {'password': 'admin'}

s = requests.Session()

r = s.get(url, params=payload, headers=headers, cookies=cookies)

cookie_value = r.cookies.get('session')
csrf_value = r.json().get('csrf')

# print(r.cookies)

# cookie_value = s.cookies.get('token')
# r = s.get(url2, cookies={'token': cookie_value})