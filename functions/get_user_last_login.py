import requests
import re

def get_last_login(token, emails):
    last_logins = []

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=88D0B4B3229647F7D1A116F34FFA7807'
        }
    
    for email in emails:
        url = "https://staging2.api.m2digitalbroker.com/proxy/amps/v2/uam/users?login={}&=".format(email)

        response = requests.request("GET", url, headers=headers, data={}, files={})

        try:
            last_login = re.findall('''.+"lastUpdated":"(.+?Z)"''', response.text)[0]
        except: 
            last_login = "error getting last login"
            print( "error getting last login for:" , email , response.text )
        last_logins.append(last_login)

    return last_logins
