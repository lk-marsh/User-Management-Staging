import json 

string = json.dumps({"access_token": "token",})

user_token = json.loads(string)["access_token"]

print(user_token)