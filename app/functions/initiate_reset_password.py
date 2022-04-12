import json 
import requests

# Returns a list of reset tokens
def initiate_reset(url, token, user_emails, user_names): 
    names = user_names
    first_names = names[0]
    last_names = names[1]

    reset_tokens = []

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
            reset_token = json.loads(response.text)["recoveryToken"]
            reset_tokens.append(reset_token)
        else:
            print("error getting activate token for",user_emails[i], response)
            reset_token = "error getting activate token"
            reset_tokens.append(reset_token)

    return reset_tokens