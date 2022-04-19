# Import library
import json

# Import environment
env:dict = json.load(open("app\env.json" , "r"))

# Import modules
from functions import get_token, get_emails ,get_user_details, get_user_status, initiate_activate_user, get_user_names, activate_user_or_password_reset, initiate_reset_password, find_inactive_emails, log_inactive_emails

# Get access token
token:str = get_token.token(env["GET_ACCESS_TOKEN_URL"])

# Get list of emails
emails:list = get_emails.emails(env["EMAIL_FILE"])

# Get user details
details:list = get_user_details.get_details(env["GET_DETAILS_URL"], token, emails)

# Determine if emails are active / inactive
statuses:list = get_user_status.get_status(details)

# Determine inactive emails
inactive_emails:list = find_inactive_emails.find_emails(emails, statuses)

# Write inactive emails to CSV file
log_inactive_emails.log_emails(env["INACTIVE_USERS_CSV_FILE"] , inactive_emails)

if len(inactive_emails) > 0:
    decision = input("There are {} inactive emails. Would you like to renew them? \ny - renew \nn - do not renew\n".format(len(inactive_emails))).strip().capitalize()
    
    if decision == "Y": 
        # Get the payload for the request to reset/activate 
        inactive_user_details:list = get_user_details.get_details(env["GET_DETAILS_URL"], token, inactive_emails)
        inactive_names:list = get_user_names.get_name(inactive_user_details)

        recovery_tokens:list = initiate_reset_password.initiate_reset(env["INITIATE_ACTIVATE_USER_URL"], token, inactive_emails, inactive_names)
        activate_user_or_password_reset.activate_or_reset(env["ACTIVATE_USER_OR_RESET_PASSWORD_URL"], token, inactive_emails, inactive_names, recovery_tokens, ["Wel@AmpWers123","Wel@AmpWers123"])
        
        print('done!')
    
    else:
        print('done!')
    
else:
    print("There are no inactive emails at the moment.")

