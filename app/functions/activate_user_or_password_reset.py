import requests
import json

def activate_or_reset(url, token, user_emails, user_names, user_tokens, new_passwords):
    statuses = []

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