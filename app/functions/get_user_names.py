# Since name is given in the user details 
from . import get_user_details

def get_name(details):
    first_names = []
    last_names = []

    for detail in details:
        try:
            first_name = detail["profile"]["firstName"]
            last_name = detail["profile"]["lastName"]
        except:
            first_name = last_name = "error getting name"
            print("error getting name for", detail)
        first_names.append(first_name)
        last_names.append(last_name)

    return [first_names, last_names]

