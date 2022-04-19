import requests
import json

def activate_or_reset(url:str, token:str, user_emails:list, user_names:list, user_tokens:list, new_passwords:list) -> list:
    statuses:list = []

    for i in range(len(user_emails)):
        payload = json.dumps({
        "login": user_emails[i],
        "firstName": user_names[0][i],
        "lastName": user_names[1][i],
        "recoveryToken": user_tokens[i],
        "newPassword": new_passwords[i]
        })
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=18C85014E143AF8CDF78EE01802E058E'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response:
            status = json.loads(response.text)["status"]
            statuses.append(status)
        else:
            print("error activating/resetting password for", user_emails[i], response)
            status = "error activating/resetting password for", user_emails[i]
            statuses.append(status)
    
    return statuses