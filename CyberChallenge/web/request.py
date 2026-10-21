import requests
import json

url = 'http://web-10.challs.olicyber.it/'
# headers = {'Accept', 'application/x-www-form-urlencoded'}
payload = {'username': 'admin', 'password': 'admin'}

r = requests.patch(url)
print(r.headers)