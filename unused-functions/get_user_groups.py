import requests


def get_groups(url: str, token: str, emails: list) -> list:
    user_groups: list = []

    for email in emails:

        request_url = url.format(email)

        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Cookie': 'JSESSIONID=A772ACD299E56998A5BC9D754B6EC840'
        }

        response = requests.request(
            "GET", request_url, headers=headers, data={}, files={})

        if response:
            user_groups.append(response.text)
        else:
            print("error getting user group for:", email, response)
            user_groups.append("error getting user group")

    return user_groups
