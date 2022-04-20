import requests
import json

# Returns access token in string
def token(url:str) -> str: 

    # Following headers given by Postman
    headers = {
        'appId': 'VMP-DI',
        'grant_type': 'client_credentials',
        'Authorization': 'Basic WTFySmVPMVZKeWg5VnBPVHR5aURZZ1YyQUF2UTZUV1k6bkMzSnNIbFFrcDJ2QVM1Mw=='
            }

    response = requests.request("GET", url, headers=headers, data={})
    
    if response: 
        user_token = json.loads(response.text)["access_token"]
    else:
        user_token = None 
        print("error: Failed to get access token", response)

    return user_token

