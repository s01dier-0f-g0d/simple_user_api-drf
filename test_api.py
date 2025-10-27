import requests

BASE_URL = "http://127.0.0.1:8000/api/users/"
response = requests.get(BASE_URL)

if response.status_code == 200:
    data = response.json().get('users', [])
    count = 1
    for user in data:
        print(f"{count}. {user['name']} - Age: {user['age']}")
        count += 1
else:
    print("Error:", response.status_code)
