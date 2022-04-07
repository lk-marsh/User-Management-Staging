# Import library
import csv 
import json

# Import environment
env = json.load(open("env.json" , "r"))

# Import modules
from functions import get_token, get_user_last_login, determine_outdated_account, get_emails 

# Get access token
token = get_token.token(env["GET_ACCESS_TOKEN_URL"])

# Get list of emails
emails = get_emails.emails(env["EMAIL_FILE"])

# Determine if emails are outdated
last_logins = get_user_last_login.get_last_login(env["GET_DETAILS_URL"], token, emails, env["LAST_LOGIN_FIELD"])
outdated = determine_outdated_account.outdated_account(last_logins, env["DAYS_BEFORE_OUTDATED"])

# Write to CSV file
fh = open(env["CSV_FILE"] , 'w')

if fh:
    writer = csv.writer(fh)
    header = ['user', 'outdated marked with X']
    data = []

    for i in range(len(emails)):
        data.append([emails[i], outdated[i]])

    writer.writerow(header)
    writer.writerows(data)

    # Success message
    print("done!")
    
else: 
    print("failed to open", env["CSV_FILE"])

