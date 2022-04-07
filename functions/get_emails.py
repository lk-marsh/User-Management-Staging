def emails(email_file):
    email_list = []
    fh = open(email_file , 'r')
    for line in fh:
        email_list.append(line.strip())

    return email_list