# Write the requests that are made to the postman (these are functions. Example: request.post)

import configuration
import requests
import data

# 1. Send a request to create a new user. Remember the authentication token (authToken).
def create_new_user ():
    headers = data.headers_create_new_user
    user_minimal_data = data.body_create_new_user_minimal_data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=headers, json=user_minimal_data)

response_create_new_user = create_new_user()
print(response_create_new_user)
print(response_create_new_user.status_code)
print(response_create_new_user.json())

authToken = response_create_new_user.json().get('authToken')


# 2. Send a request to create a personal kit for this user. Make sure to also pass the Authorization header.
def create_personal_kit (name):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {authToken}"}
    kit_body = {"name": name}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, headers=headers, json=kit_body)

response_create_personal_kit = create_personal_kit ("Max")
print(response_create_personal_kit)
print(response_create_personal_kit.status_code)
print(response_create_personal_kit.json())
