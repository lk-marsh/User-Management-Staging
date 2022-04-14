# Import Library
import unittest
import json
import httpretty

# Import environment
env = json.load(open("app/env.json" , "r"))

# Import modules
from functions import get_token, get_user_names, get_user_status, find_inactive_emails

# Mocks
mock_details = [json.loads("""{
    "profile": {
        "firstName" : "test",
        "lastName" : "ing"
            }, 
    "status" : "my_status"
}""")]

mock_emails = ["inactive email","active email"]
mock_statuses = ["INACTIVE","ACTIVE"]

def mock_get_details(url, token, emails):
    mock_get_details.calls += 1
    return mock_details


class TestToken(unittest.TestCase):
    @httpretty.activate
    def test_get_token(self):
        # define patch:
        httpretty.register_uri(httpretty.GET, env["GET_ACCESS_TOKEN_URL"],
        body = json.dumps({"access_token": "token"}))

        response = get_token.token(env["GET_ACCESS_TOKEN_URL"])

        assert response == "token"
    
    # Test getting attributes from user details
    def test_get_name(self):
        result = get_user_names.get_name(mock_details)
        assert result == [["test"],["ing"]]
        
    def test_get_status(self):
        result = get_user_status.get_status(mock_details)
        assert result == ["my_status"]
        
    def test_inactive_emails(self):
        result = find_inactive_emails.find_emails(mock_emails, mock_statuses)
        assert result == ["inactive email"]
    
if __name__ == '__main__':
    unittest.main()