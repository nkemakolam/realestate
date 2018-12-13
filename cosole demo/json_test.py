import json

userJSON = '{"first_name":"john","last_name":"nkem"}'
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'make':'Ford','model':'Mutang','year':1970}
carJSON = json.dumps(car)
print(carJSON)