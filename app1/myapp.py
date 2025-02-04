""" for retrieve data from database"""
# import requests

# URL = "http://127.0.0.1:8000/stuinfo/"

# # r = requests.get(url = URL)

# # data = r.json()

# # print(data)

"""for creating data"""

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'Sham',
    'roll' : 106,
    'city' : 'Delhi'
}
json_data = json.dumps(data)# convert python obj into json string
print("json_data of my app:-",json_data)
r = requests.post(url = URL,data = json_data)
data = r.json()
print(data)

