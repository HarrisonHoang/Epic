import csv
from ctypes import sizeof

user = "Hoa"
#print("Do you want to create(c), view(v), or edit(e) your profile?")

#input value
#name = str(input("Enter name: "))
title = str(input("Enter title: ")) #1 line of text
major = str(input("Enter major: "))
univer = str(input("Enter university: "))
about = str(input("Enter About me: "))
experi = str(input("Enter experience: "))
edu = str(input("Enter edu: "))

#first row contain the title each column
myheaders = ['name', 'title', 'major', 'univer', 'about', 'experi', 'edu']
#data value rows of csv file
myvalue = [{'name': user, 'title': title, 'major': major, 'univer': univer, 'about': about, 'experi': experi, 'edu': edu}]

#open a csv file and append value in, auto close when done
with open('profile.csv', 'a') as file:
    csv_writer = csv.DictWriter(file, fieldnames=myheaders)
    file_content = file.read        #read csv file to see if it is empty
    if file_content == "":          #check if csv file is empty
        csv_writer.writeheader()    #add myheaders (1st row in)
        csv_writer.writerows(myvalue)
    else:
        csv_writer.writerows(myvalue)

#open a csv file and read value within it, auto close when done
with open('profile.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        if line['name'] == user:
            print(line['name'])
            print(line['major'])
            print(line['edu'])