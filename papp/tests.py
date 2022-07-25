from django.test import TestCase
import requests

# login_url = 'http://127.0.0.1:8000/token/login/'
# response = requests.post(
#     login_url,
#     json  = {
#         'username': 'tpg24',
#         'password': 'admin',
#     }
# )

# print(response._content)

# url = 'http://127.0.0.1:8000/create-user/'
# response = requests.post(
#     url,
#     json = {
#             'username': 'tpg12',
#             'email': 'adesolaayodeji53@gmail.com',
#             'first_name': 'Daeji',
#             'last_name': 'pablo',
#             'password': 'theprotonguy',
#             're_password': 'theprotonguy'
#             }
#         ) 
# print(response._content)


profile_url = 'http://127.0.0.1:8000/create-profile/'
response = requests.post(
    profile_url,
    json = {
            'gender': 'm',
            'hobby': 'coding'
        },
     headers = {
        'authorization': 'Token 6c0d46d5855d6d7a2c61990e0d85e11e928d467b'
    }
)

print(response._content)