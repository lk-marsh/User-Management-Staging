# Returns a 2-dimensional list of first and last names
def get_name(details: list) -> list[list, list]:
    first_names: list = []
    last_names: list = []

    for detail in details:
        try:
            # Find values matching the keys of firstName and lastName
            first_name = detail["profile"]["firstName"]
            last_name = detail["profile"]["lastName"]
        except:
            first_name = last_name = "error getting name"
            print("error getting name for", detail)
        first_names.append(first_name)
        last_names.append(last_name)

    return [first_names, last_names]
