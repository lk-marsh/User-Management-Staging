import requests

def get_user_groups(token, emails):
    user_groups = []

    for email in emails:
        
        url = "https://services.staging.api.m2digitalbroker.com/proxy/amps/v2/uam/groups?login={}".format(email)

        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Cookie': 'JSESSIONID=A772ACD299E56998A5BC9D754B6EC840'
            }
        
        response = requests.request("GET", url, headers=headers, data={}, files={})

        if response: 
            user_groups.append(response.text)
        else:
            print("error getting user group for:" , email)
            user_groups.append("error getting user group")

get_user_groups()