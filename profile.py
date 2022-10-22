import csv

user = "Toan"

#input value
name = str(input("Enter name: "))
major = str(input("Enter major: "))
edu = str(input("enter edu: "))

# first row contain the title each column
myheaders = ['name', 'major', 'edu']
#data rows of csv file
myvalue = [{'name': name, 'major': major, 'edu': edu}]


with open('profile.csv', 'a') as file:
    csv_writer = csv.DictWriter(file, fieldnames=myheaders)
    csv_writer.writeheader()
    csv_writer.writerows(myvalue)

with open('profile.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        if line['name'] == name:
            print(line['name'])
            print(line['major'])
            print(line['edu'])