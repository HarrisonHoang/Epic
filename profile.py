import csv
import os

while True:
    user = "Nevada" #you can enter anyname in here
    option = str(input("Do you want to create(c), view(v), edit(e) your profile?"))

    if option == 'c':
        #input value
        #name = str(input("Enter name: "))
        title = str(input("Enter title: ")) #1 line of text
        major = str(input("Enter major: ")) #converted first letter upper and rest lower
        major = ' '.join(elem.capitalize() for elem in major.split())
        univer = str(input("Enter university: ")) #converted first letter upper and rest lower
        univer = ' '.join(elem.capitalize() for elem in univer.split())
        about = str(input("Enter About me: ")) #1 paragraph of text
        print("For experience, you can insert up to 3 past jobs. If none, enter 0" + 
            "(include title, employer, data started and ended, location, and describe what you did")
        experi1 = str(input("Enter lastest experience: "))
        experi2 = str(input("Enter 2nd experience: "))
        experi3 = str(input("Enter 3th experience: "))
        edu = str(input("Enter education (include school name, degree, and years attended: "))

        #first row contain the title each column
        myheaders = ['name', 'title', 'major', 'univer', 'about', 'experi1', 'experi2', 'experi3', 'edu']
        #data value rows of csv file
        myvalue = [{'name': user, 'title': title, 'major': major, 'univer': univer, 'about': about, 'experi1': experi1, 'experi2': experi2, 'experi3': experi3, 'edu': edu}]

        #open a csv file and append value in, auto close when done
        with open('profile.csv', 'a') as file:
            csv_writer = csv.DictWriter(file, fieldnames=myheaders)
            check_file = os.stat('profile.csv').st_size  #read csv file to see if it is empty
            if(check_file == 0):        #check if csv file is empty
                csv_writer.writeheader()    #add myheaders (1st row in)
                csv_writer.writerows(myvalue)
            else:
                csv_writer.writerows(myvalue)

    if option == 'v':
        #open a csv file and read value within it, auto close when done
        with open('profile.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                if line['name'] == user:
                    print("\nProfile of: " + line['name'])
                    print("Title: " + line['title'])
                    print("Major: " + line['major'])
                    print("University: " + line['univer'])
                    print("About me: " + line['about'])
                    print("Experience 1: " + line['experi1'])
                    print("Experience 2: " + line['experi2'])
                    print("Experience 3: " + line['experi3'])
                    print("Education: " + line['edu'])


    if option == 'x':
        break
    print("\nPress (x) to quit\n")