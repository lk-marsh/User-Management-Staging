import json 
import requests

# Returns a list of activation tokens
def initiate_activate(url, token, user_emails, user_names) -> list: 
    if len(user_emails) != len(user_names):
        print("Error: Email and Names lists don't match.")
        return

    names = user_names
    first_names = names[0]
    last_names = names[1]

    activate_tokens:list = []

    for i in range(len(user_emails)): 
        payload = json.dumps({
            "login": user_emails[i],
            "firstName": first_names[i],
            "lastName": last_names[i]
        })

        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=76EB7FB1E167DF743285F78E2F0DC405'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response:
            activate_token = json.loads(response.text)["recoveryToken"]
            activate_tokens.append(activate_token)
        else:
            print("error getting activate token for",user_emails[i], response)
            activate_token = "error getting activate token"
            activate_tokens.append(activate_token)

    return activate_tokens