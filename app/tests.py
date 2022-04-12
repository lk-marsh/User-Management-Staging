# Import Library
import unittest
import json
import httpretty
import trace

# Import environment
env = json.load(open("app/env.json" , "r"))

# Import modules
from functions import get_token, get_user_details, get_user_names, get_user_status

# Mocks
mock_details = [json.loads("""{
    "profile": {
        "firstName" : "test",
        "lastName" : "ing"
            }, 
    "status" : "my_status"
}""")]


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
        get_user_status.get_status.assert_called_once()
    
    # def test_get_details(self):
    #     details = json.dumps({"details" : "details"})
    #     httpretty.register_uri(httpretty.GET, env["GET_DETAILS_URL"],
    #     body = details,
    #     status = 200)

    #     response = get_user_details.get_details(env["GET_DETAILS_URL"], "token", ["emails"])
    #     print(response)

    #     assert response == details

    # def test_one(self):
    #     # define your patch:
    #     httpretty.register_uri(httpretty.GET, env["GET_ACCESS_TOKEN_URL"],
    #                         body="Find the best daily deals")
    #     # use!
    #     response = requests.get(env["GET_ACCESS_TOKEN_URL"])
    #     assert response.text == "Find the best daily deals"

    # def test_request_get(self):
    #     with patch("requests.get") as patched_get:
    #         token = get_token.token(env["GET_ACCESS_TOKEN_URL"])
    #         print(token)

    #         patched_get.assert_called_once_with(env["GET_ACCESS_TOKEN_URL"])



# def mocked_requests_get(*args, **kwargs):
#     response_content = None
#     request_url = kwargs.get('url', None)
#     if request_url == 'get_token':
#         response_content = json.dumps({"access_token":'token'})
#     elif request_url == 'burl':
#         response_content = json.dumps('b response')
#     elif request_url == 'curl':
#         response_content = json.dumps('c response')
#     response = Response()
#     response.status_code = 2123213221
#     response._content = str.encode(response_content)
#     return response
    

    


# class TestGetToken(unittest.TestCase):
#     @mock.patch('functions.get_token.requests.get', side_effect=mocked_requests_get)

#     # def test_fetch(self, mock_get):
#     #     response = get_token.requests.get(url="get_token")
#     #     self.assertEqual(response._content, b'{"access_token": "token"}')
    
#     def returns_token_if_url_valid(self):
#         with mock.patch('functions.get_token.requests.get') as mock_requests_get:
#             mock_requests_get.return_value.text = '''"access_token" : "token", '''
#             request = get_token.token("https://staging2.api.m2digitalbroker.com/proxy/amps/v2/oauth/accesstoken")
#         self.assertEqual(request , "token")

if __name__ == '__main__':
    unittest.main()