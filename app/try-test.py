# Import Library
import json
import unittest.mock
import httpretty

# Import environment
env = json.load(open("app/env.json" , "r"))

# Import modules
from functions import get_token, get_user_names, get_user_status, find_inactive_emails, get_emails, initiate_activate_user

# Mocks
mock_emails = ["inactive email","active email"]
mock_names = ["Mr Inactive", "Mrs Active"]


class TestToken(unittest.TestCase):
    @httpretty.activate

    def test_get_token(self):
        # define patch:
        httpretty.register_uri(httpretty.GET, env["GET_ACCESS_TOKEN_URL"],
        body = json.dumps({"access_token": "token"}))

        response = get_token.token(env["GET_ACCESS_TOKEN_URL"])

        print(response)
        assert response == "token"


    
if __name__ == '__main__':
    unittest.main()
