import requests
import json

# Returns a list of python dictionary of user's details
def get_details(url, token, emails):
    details = []

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=88D0B4B3229647F7D1A116F34FFA7807'
        }
    
    for email in emails:
        request_url = url.format(email)

        response = requests.request("GET", request_url, headers=headers, data={}, files={})
        
        if response:
            details.append(json.loads(response.text))
        else:
            print('error getting user details for', email, response)
            details.append("error getting user details")
    
    return (details)