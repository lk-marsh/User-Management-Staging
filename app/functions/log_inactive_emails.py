import csv 

def log_emails(file, emails):
    fh = open(file, 'w')

    if fh:
        writer = csv.writer(fh)
        header = ['inactive users']
        
        writer.writerow(header)
        for email in emails:
            writer.writerow([email])
    else:
        print("error opening file",file)