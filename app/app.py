# Import library
import csv 
import json

# Import environment
env = json.load(open("app\env.json" , "r"))

# Import modules
from functions import get_token, get_emails ,get_user_details, get_user_status, initiate_activate_user, get_user_names, activate_user_or_password_reset, initiate_reset_password
# print(get_user_status.get_status("https://staging2.api.m2digitalbroker.com/proxy/amps/v2/uam/users?login={}&=", "UX8PHTFheC5sTtuGmZs9d8erPKCN" , ['leng-khai.ang@marsh.com', 'mahesh.cv@marsh.com'] ))

# Get access token
token = get_token.token(env["GET_ACCESS_TOKEN_URL"])

# Get list of emails
emails = get_emails.emails(env["EMAIL_FILE"])
test_emails = ["bendover6671011@gmail.com", "lengkhai@gmail.com"]
test_names = [["Ben", "l"],["Dover","k"]]

# Get user details
details = get_user_details.get_details(env["GET_DETAILS_URL"], token, emails)
# Determine if emails are active / inactive
statuses = get_user_status.get_status(details)
# print(statuses)

inactive_emails = []

for i in range(len(emails)): 
    print(emails[i], ':', statuses[i])
    if statuses[i] == "RECOVERY":
        inactive_emails.append(emails[i])

# Write inactive emails to CSV file
fh = open(env["INACTIVE_USERS_CSV_FILE"], 'w')
if fh:
    writer = csv.writer(fh)
    header = ['inactive users']
    
    writer.writerow(header)
    for email in inactive_emails:
        writer.writerow([email])

# decision = input("There are {} inactive emails. Would you like to renew them? \ny - renew \nn - do not renew\n".format(len(inactive_emails))).strip().capitalize()
decision = "Y"

if decision == "Y": 
    inactive_user_details = get_user_details.get_details(env["GET_DETAILS_URL"], token, inactive_emails)
    names = get_user_names.get_name(inactive_user_details)

    #test
    recovery_tokens = initiate_reset_password.initiate_reset(env["INITIATE_ACTIVATE_USER_URL"], token, test_emails, test_names)
    activate_user_or_password_reset.activate_or_reset(env["ACTIVATE_USER_OR_RESET_PASSWORD_URL"], token, test_emails, test_names, recovery_tokens, ["Wel@AmpWers123","Wel@AmpWers123"])
    print('done!')
else:
    print('done!')