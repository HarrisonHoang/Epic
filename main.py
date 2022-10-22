import json

with open('userprofile.json') as f:
    data = json.load(f)
    #check if key exists in JSON
    if "profile" in data:
        print("Key exist")
    else:
        print("Key DNE")
    #check if a value for a key in JSON
    if 'name' in data['profile']:
        print("value is exist")
        print(data.get('name'))
    else:
        print("Value DNE")

    #print specific data in nested JSON data
    '''
    print (data['profile'][0]['name'])
    print (data['profile'][0]['title'])
    print (data['profile'][0]['info'])'''
'''



for prof in data['profile']:
    inputU = str(input("Enter name: "))
    if prof['name'] == inputU:
        print(prof['name'], prof['title'])
        print(prof['info'])
    else:
        continue'''


'''
#func to add to json
def write_json(new_data, filename = 'userprofile.json'):
    with open(filename,'r+') as file:
        #first we load existing file_data into a dict.
        file_data = json.load(file)
        #join new_data with file_data inside "profile"
        file_data["profile"].append(new_data)
        #sets file's current position at offset
        file.seek(0)
        #convert back to json
        json.dump(file_data, file, indent=4)

a = input()
#python object to be appended
y = {"name": a,
     "major": "CE",
     "about": "Full time"
    }

write_json(y)
'''




# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent = 2)