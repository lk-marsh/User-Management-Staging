import csv 

def log_emails(file:str, emails:list) -> None:
    fh = open(file, 'w')

    if fh:
        writer = csv.writer(fh)
        header = ['inactive users']
        
        writer.writerow(header)
        for email in emails:
            writer.writerow([email])
        print("Logged inactive emails to",file)
    else:
        print("error opening file",file)