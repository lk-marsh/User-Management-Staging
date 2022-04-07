from contextlib import nullcontext
import requests
import re

def token(): 
    url = "https://staging2.api.m2digitalbroker.com/proxy/amps/v2/oauth/accesstoken"
    headers = {
        'appId': 'VMP-DI',
        'grant_type': 'client_credentials',
        'Authorization': 'Basic WTFySmVPMVZKeWg5VnBPVHR5aURZZ1YyQUF2UTZUV1k6bkMzSnNIbFFrcDJ2QVM1Mw=='
            }

    response = requests.request("GET", url, headers=headers, data={})

    try:
        user_token = re.findall('''.+"access_token" : "(.+)?",''',response.text)[0]
    except:
        user_token = None 
        print("error: Failed to get access token")

    return user_token

