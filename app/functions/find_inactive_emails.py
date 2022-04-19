def find_emails(emails:list, statuses:list) -> list:
    inactive_emails:list = []

    for i in range(len(emails)): 
        print(emails[i], ':', statuses[i])
        if statuses[i] == "INACTIVE":
            inactive_emails.append(emails[i])

    return inactive_emails