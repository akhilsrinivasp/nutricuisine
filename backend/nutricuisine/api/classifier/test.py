import requests

url = "http://0.0.0.0:5051//predict"

payload = {}
files=[
  ('file',('Tomato.jpg',open('/Users/akhilsp/Downloads/Tomato.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
