import requests

def get_details(url, token, emails):
    details = []

    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Cookie': 'JSESSIONID=88D0B4B3229647F7D1A116F34FFA7807'
        }
    
    for email in emails:
        request_url = url.format(email)

        response = requests.request("GET", request_url, headers=headers, data={}, files={}).text
        
        if response:
            details.append(response)
        else:
            print('error getting user details for', email)
            details.append("error getting user details")
    
    return details

# print(get_details("https://staging2.api.m2digitalbroker.com/proxy/amps/v2/uam/users?login={}&=", "7xIwBnSRy2nAbibjG0kBGSJVUGBa", ["leng-khai.ang@marsh.com" , "mahesh.cv@marsh.com"]))