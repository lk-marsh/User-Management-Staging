import zulu

def outdated_account(last_logins:list, days_before_expiry:str) -> list:
    current_time = zulu.now()
    six_days_ago = current_time.shift(days = -int(days_before_expiry))

    outdated:list = []

    for login in last_logins:
        try:
            zulu_login = zulu.parse(login)
            if six_days_ago > zulu_login:
                outdated.append('X')
            else:
                outdated.append("")
        except:
            print("error converting login time:", login)
            outdated.append("ERROR")

    return outdated
