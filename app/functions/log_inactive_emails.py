import csv 

def log_emails(fh, emails:list) -> None:
    if fh:
        writer = csv.writer(fh)
        header = ['inactive users']
        
        writer.writerow(header)
        for email in emails:
            writer.writerow([email])
        print("Logged inactive emails to",fh.name)
    else:
        print("error opening file",fh.name)