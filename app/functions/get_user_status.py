# Returns a list of statuses
def get_status(details: list) -> list:
    statuses: list = []

    for detail in details:
        try:
            # Finds values matching the "status" key
            status = detail["status"]
        except:
            status = "error getting status"
            print("error getting status for:", detail)
        statuses.append(status)

    return statuses
