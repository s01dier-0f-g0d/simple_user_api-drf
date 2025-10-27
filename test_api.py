import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/users/"

response = requests.get(BASE_URL)

print("Raw Response:")
print(response.text)
print("-" * 50)

if response.status_code == 200:
    try:
        user_profiles = response.json()
    except json.JSONDecodeError:
        print("Response is not valid JSON!")
        exit()

    # Check if it's a dict instead of a list
    if isinstance(user_profiles, dict):
        print("Response is a dictionary, not a list.")
        print(json.dumps(user_profiles, indent=4))
        exit()

    print("All User Profiles:\n" + "-" * 50)

    count = 1
    for user in user_profiles:
        print(f"{count}. Name: {user['name']}")
        print(f"   Date of Birth: {user['date_of_birth']}")

        if 'age' in user:
            print(f"   Age: {user['age']}")
        print("-" * 50)
        count += 1
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    print(response.text)
