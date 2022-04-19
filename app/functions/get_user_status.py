# Since last login is given in the user details 
from . import get_user_details

def get_status(details:list) -> list:
    statuses:list = []

    for detail in details: 
        try: 
            status = detail["status"]
        except:
            status = "error getting status"
            print( "error getting status for:" , detail)
        statuses.append(status)

    return statuses

