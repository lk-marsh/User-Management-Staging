# Returns a list of emails with statuses of "INACTIVE"
def find_emails(emails: list, statuses: list) -> list:
    inactive_emails: list = []

    # Search for INACTIVE statuses
    for i in range(len(emails)):
        print(emails[i], ':', statuses[i])
        if statuses[i] == "INACTIVE":
            inactive_emails.append(emails[i])

    return inactive_emails
