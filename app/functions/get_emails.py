def emails(fh) -> list:
    email_list:list = []
    if fh:
        for line in fh:
            email_list.append(line.strip())

        return email_list
    else:
        print("failed to open", fh.name)
        return email_list