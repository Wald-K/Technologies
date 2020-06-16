import requests
import json




name = 'Patryk'

user = {'user': name}
user_json = json.dumps(user)




# r = requests.post('http://localhost:5000/checkin', data=user_json)

r = requests.post('http://localhost:5000/checkin', json={'user': name})
print(r.status_code)




