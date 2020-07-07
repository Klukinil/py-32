from pprint import pprint

import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 7532975

OAUTH_DATA = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'status,audio',
    'response_type': 'token',
    'v': 5.120,
    'redirect_uri': 'https://example.com/'
}

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_DATA))
))

# TOKEN = '959ee46eb78b742b5ee80bb968704aef92da579b4035475e70df4a7a5df432b0a6cbfb6eaa04dcd431f4b'
#
#
# def get_status(token):
#     response = requests.get(
#         'https://api.vk.com/method/status.get',
#         params={
#             'access_token': token,
#             'v': 5.21
#         }
#     )
#     return response.json()
#
#
# def set_status(token, text):
#     response = requests.get(
#         'https://api.vk.com/method/status.set',
#         params={
#             'access_token': token,
#             'v': 5.21,
#             'text': text
#         }
#     )
#     return response.json()
#
#
# status = get_status(TOKEN)
# set_status(TOKEN, 'some status')
#
#
# class User:
#     def __init__(self, token) -> None:
#         self.token = token
#
#     def get_status(self):
#         response = requests.get(
#             'https://api.vk.com/method/status.get',
#             params={
#                 'access_token': self.token,
#                 'v': 5.21
#             }
#         )
#         return response.json()
#
#     def set_status(self, text):
#         response = requests.get(
#             'https://api.vk.com/method/status.set',
#             params={
#                 'access_token': self.token,
#                 'v': 5.21,
#                 'text': text
#             }
#         )
#         return response.json()
#
#
# artyom = User(TOKEN)
# artyom.get_status()
# artyom.set_status('Another hello!')
