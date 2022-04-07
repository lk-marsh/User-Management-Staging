import requests

def get_details(token, emails):
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=88D0B4B3229647F7D1A116F34FFA7807'
        }
    
    for email in emails:
        url = "https://staging2.api.m2digitalbroker.com/proxy/amps/v2/uam/users?login={}&=".format(email)

        response = requests.request("GET", url, headers=headers, data={}, files={}).text
        
        if response:
            print(response)
        else:
            print('error getting user details for', email)
