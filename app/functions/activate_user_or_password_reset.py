import requests
import json

# Sends the POST request to actually reset/activate the users. Returns a list of statuses
def activate_or_reset(url:str, token:str, user_emails:list, user_names:list, user_tokens:list, new_passwords:list) -> list:
    if (len(user_emails) == len(user_names) == len(user_tokens) == len(new_passwords)) == False:
        print("Error: Lists of Emails, Names, Recovery Tokens and Passwords don't match!")
        return

    statuses:list = []

    for i in range(len(user_emails)):
        # Following the payloads and headers given by Postman
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

        # Return the value of key "status"
        if response:
            status = json.loads(response.text)["status"]
            statuses.append(status)
        else:
            print("error activating/resetting password for", user_emails[i], response)
            status = "error activating/resetting password for", user_emails[i]
            statuses.append(status)
    
    return statuses