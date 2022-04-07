import re

# Since last login is given in the user details 
from . import get_user_details

def get_last_login(url, token, emails, field):
    last_logins = []
    details = get_user_details.get_details(url, token, emails)

    for detail in details: 
        try:
            last_login = re.findall('''.+"{}":"(.+?Z)"'''.format(field), detail)[0]
        except:
            last_login = "error getting last login"
            print( "error getting last login for:" , detail )
            
        last_logins.append(last_login)

    return last_logins