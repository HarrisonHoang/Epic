import json

#load the data from json file
with open('states.json') as f:
    data = json.load(f)

#print elem of the data states
for state in data['states']:
    print(state['name'], state['abbreviation'])
    del state['area_codes'] #delete the elem area_code

#write data to the json file
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent = 2)

print(len(state['name']))