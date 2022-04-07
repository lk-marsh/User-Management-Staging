#import library
import csv 

#import modules
from functions import get_token, get_user_last_login, determine_outdated_account, get_emails

#set variables
email_file = r"C:\Users\u1261919\OneDrive - MMC\Documents\user-management-staging\User-Management-Staging\emails.txt"
csv_file = r"C:\Users\u1261919\OneDrive - MMC\Documents\user-management-staging\User-Management-Staging\users-last-login.csv"
days_before_expiry = 6

#get access token
token = get_token.token()

#get list of emails
emails = get_emails.emails(email_file)

#determine if emails are outdated
if token:
    last_logins = get_user_last_login.get_last_login(token, emails)
    outdated = determine_outdated_account.outdated_account(last_logins, days_before_expiry)

fh = open(csv_file , 'w')
writer = csv.writer(fh)

header = ['user', 'outdated marked with X']
data = []

for i in range(len(emails)):
    data.append([emails[i], outdated[i]])

writer.writerow(header)
writer.writerows(data)
print("done!")