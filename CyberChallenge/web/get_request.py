import requests 

url = 'https://files.learn.esadecimale.it/chal/cc-web-1.mp4'
# payload = {'id': 'flag'}
headers = {'Referer': 'cc2026'}
# cookies = dict(password='admin')

# s = requests.Session()
# r = requests.get(url)
r = requests.get(url, headers=headers)
print(r.text)
# print(r.cookies)

# r2 = s.get('http://web-06.challs.olicyber.it/flag', cookies=r.cookies)
# print(r2.text)