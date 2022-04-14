def find_emails(emails, statuses):
    inactive_emails = []

    for i in range(len(emails)): 
        print(emails[i], ':', statuses[i])
        if statuses[i] == "INACTIVE":
            inactive_emails.append(emails[i])

    return inactive_emails