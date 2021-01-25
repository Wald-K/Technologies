import os
import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"

AUTH_ENDPOINT = "http://127.0.0.1:8000/auth/jwt/"


# def do(method='GET', data={}, is_json=True):
#     headers = {}
#     headers['Content-type'] = 'application/json'
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers= headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do(method='put', data={"id": 8, "user":1, "content":"Quite new content"})
# do(method='delete', data={"id": 8})




#--------------------------------------
# test with file data in put method
image_path = os.path.join(os.getcwd(), "logo.png")


# def do_img(method='GET', data={}, is_json=True, img_path=None):
#     headers = {}
#     headers['Content-type'] = 'application/json'
#     if is_json:
#         data = json.dumps(data)

#     if img_path is not None:
#         with open(image_path, 'rb') as image_handler:
#             file_data = {'image': image_handler}
#             r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do_img(method='POST', data={'user': 1, "content":"YYYYYYYYYYY"} , is_json=False, img_path=image_path)
# do_img(method='PUT', data={'user': 1, "id": 8, "content":"zzzzzzzzzzzzzzzzz"}, is_json=True)
# do_img(method='PUT', data={'user': 1, "id": 8, "content":"zzzzzzzzzzzzzzzzz"}, is_json=True)





def do_2_endpoints(id, method='GET', data={}, is_json=True, img_path=None):
    headers = {}
    headers['Content-type'] = 'application/json'
    if is_json:
        data = json.dumps(data)

    if img_path is not None:
        with open(image_path, 'rb') as image_handler:
            file_data = {'image': image_handler}
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT + str(id)+ "/", data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


def do_2_endpoints_get(id=None, method='GET', data={}, is_json=True, img_path=None):
    headers = {}
    headers['Content-type'] = 'application/json'
   
    if id is not None:
        r = requests.request(method, ENDPOINT + str(id)+"/", headers=headers)
    else:
        r = requests.request(method, ENDPOINT, headers=headers)

    print(r.text)
    print(r.status_code)
    return r

# do_2_endpoints(method='GET', id=8, is_json=True, img_path=None) -> GET

# data = {"id": 8, "user": 1, "content": "ABCDEF"}
# do_2_endpoints(method='PUT', id=8, data=data, is_json=True, img_path=None)   ->PUT

# do_2_endpoints_get(id=5, method='GET')


####### JWT ##########

# obtain token
# login_data = {'username': 'wald', 'password': 'Test@720318'}
# headers = {}
# headers['Content-type'] = 'application/json'
# r = requests.post(AUTH_ENDPOINT+'api-token-auth/', data=json.dumps(login_data), headers=headers)
# print(r.text)

# refresh token
# token_data = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndhbGQiLCJleHAiOjE2MTE0OTU2NTEsImVtYWlsIjoid0BvcC5wbCIsIm9yaWdfaWF0IjoxNjExNDk1MzUxfQ.Yf4fST6KNgafIu41qO8ot-939izIebUU9_O7N5JzTZA'}
# headers = {}
# headers['Content-type'] = 'application/json'
# r = requests.post(AUTH_ENDPOINT+'api-token-refresh/', data=json.dumps(token_data), headers=headers)
# print(r.text)

# verify token
# token_to_verify = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndhbGQiLCJleHAiOjE2MTE0OTU2NTEsImVtYWlsIjoid0BvcC5wbCIsIm9yaWdfaWF0IjoxNjExNDk1MzUxfQ.Yf4fST6KNgafIu41qO8ot-939izIebUU9_O7N5JzTZA'}
# headers = {}
# headers['Content-type'] = 'application/json'
# r = requests.post(AUTH_ENDPOINT+'api-token-verify/', data=json.dumps(token_to_verify), headers=headers)
# print(r.status_code)



## teraz żądanie POST z tokenem

# obtain token
login_data = {'username': 'wald', 'password': 'Test@720318'}
headers = {}
headers['Content-type'] = 'application/json'
r = requests.post(AUTH_ENDPOINT+'api-token-auth/', data=json.dumps(login_data), headers=headers)

token = r.json()['token']

post_data = {'content': 'Fajna treść'}

headers = {}
headers['Content-type'] = 'application/json'
headers['Authorization'] = 'JWT ' + token


post_request = requests.post(ENDPOINT, data=json.dumps(post_data), headers=headers)
print(post_request.text)


