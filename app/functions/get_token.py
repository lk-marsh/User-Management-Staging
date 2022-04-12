import requests
import json

def token(url): 
    headers = {
        'appId': 'VMP-DI',
        'grant_type': 'client_credentials',
        'Authorization': 'Basic WTFySmVPMVZKeWg5VnBPVHR5aURZZ1YyQUF2UTZUV1k6bkMzSnNIbFFrcDJ2QVM1Mw=='
            }

    response = requests.request("GET", url, headers=headers, data={})
    if response: 
        user_token = json.loads(response.text)["access_token"]
        # user_token = re.findall('''.+"access_token" : "(.+)?",''',response.text)[0]
    else:
        user_token = None 
        print("error: Failed to get access token", response)

    return user_token

