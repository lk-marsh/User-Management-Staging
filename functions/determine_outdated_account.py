import zulu

def outdated_account(last_logins, days_before_expiry):
    current_time = zulu.now()
    six_days_ago = current_time.shift(days = -days_before_expiry)
    # print(current_time)

    outdated = []

    for login in last_logins:
        zulu_login = zulu.parse(login)

        if six_days_ago > zulu_login:
            outdated.append('X')
        else:
            outdated.append("")

    return outdated
