# Import Library
import json
import unittest.mock
import httpretty

# Import environment
env = json.load(open("app/env.json" , "r"))

# Import modules
from functions import get_token, get_user_names, get_user_status, find_inactive_emails, get_emails, log_inactive_emails

# Mocks
url = "mockurl"
token = "mocktoken"
mock_emails = ["inactive email","active email"]
mock_inactive_emails = ["inactive email 1", "inactive email 2"]
mock_statuses = ["INACTIVE","ACTIVE"]
mock_names = ["Mr Inactive", "Mrs Active"]

mock_details = [json.loads("""{
    "profile": {
        "firstName" : "test",
        "lastName" : "ing"
            }, 
    "status" : "my_status"
}""")]

mock_user_tokens = ["token", "token"]
mock_new_passwords = ["abc", "123"]

def mock_get_details(url, token, emails):
    return mock_details * len(emails)

def mock_initiate_activate_user(url, token, user_emails, user_names):
    return [token] * len(user_emails)

def mock_initiate_reset_password(url, token, user_emails, user_names):
    return [token] * len(user_emails)

def mock_activate_or_reset(url, token, user_emails, user_names, user_tokens, new_passwords):
    return [200] * len(user_emails)

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
        print(result)
        assert result == ["inactive email"]

    def test_get_details(self):
        result = mock_get_details(url, token, mock_emails)
        self.assertEqual(len(result), 2)

    def test_initiate_activate_user(self):
        result = mock_initiate_activate_user(url, token, mock_emails, mock_names)
        self.assertEqual(len(result), 2)

    def test_initiate_reset_password(self):
        result = mock_initiate_reset_password(url, token, mock_emails, mock_names)
        self.assertEqual(len(result), 2)        

    def test_activate_or_reset(self):
        result = mock_activate_or_reset(url, token, mock_emails, mock_names, mock_user_tokens, mock_new_passwords)
        self.assertEqual(len(result), 2)

    def test_read_email_file(self):
        with unittest.mock.patch('__main__.open', unittest.mock.mock_open(read_data="email1\nemail2")) as m:
            with open('mock/email/file/path') as h:
                emails = get_emails.emails(h)
        m.assert_called_once_with('mock/email/file/path')
        assert emails == ["email1","email2"]
    
    def test_write_file(self):
        m = unittest.mock.mock_open()
        with unittest.mock.patch('__main__.open', m):
            with open('mock/inactive/emails/log/path','w') as h:
                log_inactive_emails.log_emails(h, mock_inactive_emails)
        handle = m()

        calls_list = handle.write.call_args_list

        # Header + 2 emails
        self.assertEqual(handle.write.call_count, 3)

        # Header of CSV File
        self.assertEqual(calls_list[0] , unittest.mock.call('inactive users\r\n') )

        # Contents of CSV
        self.assertEqual(calls_list[1] , unittest.mock.call('inactive email 1\r\n') )
        self.assertEqual(calls_list[2] , unittest.mock.call('inactive email 2\r\n') )

        
if __name__ == '__main__':
    unittest.main()
