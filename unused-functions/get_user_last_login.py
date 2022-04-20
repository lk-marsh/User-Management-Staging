# Since last login is given in the user details
from . import get_user_details


def get_last_login(details: list, field: str) -> list:
    last_logins: list = []

    for detail in details:
        try:
            last_login = detail[field]
        except:
            last_login = "error getting last login"
            print("error getting last login for:", detail)

        last_logins.append(last_login)

    return last_logins
