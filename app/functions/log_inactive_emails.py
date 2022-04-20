import csv 

# Write a list of emails into a CSV file given a file handler
def log_emails(fh, emails:list) -> None:
    if fh:
        writer = csv.writer(fh)
        header = ['inactive emails']
        
        writer.writerow(header)
        for email in emails:
            writer.writerow([email])
        print("Logged {} inactive emails to {}".format(len(emails), fh.name))
    else:
        print("error opening file",fh.name)