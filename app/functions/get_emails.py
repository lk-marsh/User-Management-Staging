def emails(email_file:str) -> list:
    email_list:list = []
    fh = open(email_file , 'r')
    if fh:
        for line in fh:
            email_list.append(line.strip())

        return email_list
    else:
        print("failed to open", email_file)
        return email_list