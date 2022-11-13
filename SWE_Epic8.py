import csv
import os
import json

#Global Variables
user = "" 
userTier = ""
Request = {}
friends = {}
jobDeleted = 0
messageCount = 0
allUsers = []
for line in open("allUsers.txt", "r").readlines():
    allUsers.append(line.replace("\n", ""))

#with open('friends.json', 'r') as friends_json:
#   friends = json.load(friends_json)

#Make notification if the user is in the list of all users
def notification(forUser, notifMessage):
    if forUser in allUsers:
        notificationsFile = open("notifications.txt", "r")
        notificationsFile.write(forUser)
        notificationsFile.write(" ")
        notificationsFile.write(notifMessage)
        notificationsFile.write("\n")
        notificationsFile.close()

#prints notfications
def readNotifications():
    for line in open("notifications.txt", "r").readlines():
        notif = line.split()
        if notif[0] == user:
            print(notif[1])
            #Remove notification after being printed


#AFTER LOGIN = HOME PAGE
#created a function in order to call it again when asked to return to the main screen
def additionalOptions():
    global user
    addiOption = str(input("\nPress J to search for a job:\n"
                        "Press V to view or edit your PROFILE:\n"
                        "Press F to find someone you know:\n"
                        "Press S to learn a new skill:\n"
                        "Press N to see your network:\n"
                        "Press P to see pending friend requests: \n"
                        "Press M to send a message\n"
                        "Or, enter InCollege Important Links to view important InCollege links\n"))
    if addiOption == "J" or addiOption == "j":
        jobSearch(user, jobDeleted)

    elif addiOption == "V" or addiOption == "v":
        profile()

    elif addiOption == "F" or addiOption == "f":
        SearchPeople2()

    #after selecting learn new skill, present 5 skills for user to select or return
    elif addiOption == "S" or addiOption == "s":
        skill = str(input("\nSelect one of these five skills:\n"
                        "   coding practice\n"
                        "   new language\n"
                        "   jira\n"
                        "   github\n"
                        "   excel\n"
                        "\n return\n"))
        if skill == "coding practice":
            print("\nUnder construction\n")
        if skill == "new language":
            print("\nUnder construction\n")
        if skill == "jira":
            print("\nUnder construction\n")
        if skill == "github":
            print("\nUnder construction\n")
        if skill == "excel":
            print("\nUnder construction\n")
        #for return, call function again
        if skill == "return":
            additionalOptions()
    elif addiOption == "N" or addiOption == "n":
        network(user)
    elif addiOption == "P" or addiOption == "p":
        friendRequest()
    elif addiOption == "M" or addiOption == "m":
        Messages()
    elif addiOption == "InCollege Important Links":
        ImportantLinks()
    else:
        additionalOptions()

# Edit: additionalOption(), profile()
def profile():
    while user: #while user has a value, aka the user is logged in
        option = str(input("Do you want to create(c), view(v), edit(e) your profile? "))

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

        if option == 'e':
            #open a csv file and read value within it, auto close when done
            with open('profile.csv', 'r+') as file:
                csv_reader = csv.DictReader(file)
                for line in csv_reader:
                    if line['name'] == user:
                        print("\nProfile of: " + line['name'])
                        print("Note: Press 'e' if edit, press k to keep. ")
                        
                        print("Title: " + line['title'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            title = str(input("Enter title: "))
                        #if choice == 'k':
                        else:
                            #continue
                            title = line['title']

                        print("Major: " + line['major'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            major = str(input("Enter major: "))
                        #if choice == 'k':
                        else:
                            #break
                            major = line['major']

                        print("University: " + line['univer'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            univer = str(input("Enter univer: "))
                        #if choice == 'k':
                        else:
                            #break
                            univer = line['univer']

                        print("About me: " + line['about'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            about = str(input("Enter about: "))
                        #if choice == 'k':
                        else:
                            #break
                            about = line['about']

                        print("Experience 1: " + line['experi1'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            experi1 = str(input("Enter experi1: "))
                        #if choice == 'k':
                        else:
                            #break
                            experi1 = line['experi1']

                        print("Experience 2: " + line['experi2'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            experi2 = str(input("Enter experi2: "))
                        #if choice == 'k':
                        else:
                            #break
                            experi2 = line['experi2']

                        print("Experience 3: " + line['experi3'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            experi3 = str(input("Enter experi3: "))
                        #if choice == 'k':
                        else:
                            #break
                            experi3 = line['experi3']

                        print("Education: " + line['edu'])
                        choice = (str(input("Edit[e] or keep[k]")))
                        if choice == 'e':
                            edu = str(input("Enter edu: "))
                        #if choice == 'k':
                        else:
                            #break
                            edu = line['edu']
                    break

                #first row contain the title each column
                myheaders = ['name', 'title', 'major', 'univer', 'about', 'experi1', 'experi2', 'experi3', 'edu']

                #data value rows of csv file
                myvalue = [{'name': user, 'title': title, 'major': major, 'univer': univer, 'about': about, 'experi1': experi1, 'experi2': experi2, 'experi3': experi3, 'edu': edu}]

                csv_writer = csv.DictWriter(file, fieldnames=myheaders)
                csv_writer.writerows(myvalue)


        if option == 'x':
            General()
        print("\nPress (x) to quit\n")

def display(user):
    search = str(input("Enter a name of your friend to view their profile"))
    result = friends["name"].count(search)
    if result > 0:
        with open('profile.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                if line['name'] == search:
                    print("\nProfile of: " + line['name'])
                    print("Title: " + line['title'])
                    print("Major: " + line['major'])
                    print("University: " + line['univer'])
                    print("About me: " + line['about'])
                    print("Experience 1: " + line['experi1'])
                    print("Experience 2: " + line['experi2'])
                    print("Experience 3: " + line['experi3'])
                    print("Education: " + line['edu'])
                else:
                    print("User does not have a profile")
    else:
        print("User is not in your friends list")


def network(user):
    temp2 = []
    friend = str(input("How would you like your new friend's name stored in your friend's list?"))
    temp2.append(friend)#list containing friend input
    #Changed to make friends a json file *changed during epic 7*


    friends[user].append(temp2)#appends to user friend list in dictionary  
    temp = []
    temp.append(user)
    Request[friend].append(temp)
    viewList = str(input("Would you like to see your network"))
    if viewList == "Yes" or viewList == "yes":
        print(friends[user])
    if viewList == "No" or viewList == "no":
        return
    friendRemoval = str(input("Would you like to remove a friend?"))
    if friendRemoval == "yes":
        #Change!!!!!!
        remove = str(input("Who would you like to remove?"))
        friends[user].remove(remove)
        friends[remove].remove(user)
        if (user) not in friends:
            print("You are currently not friends")
            return
    if friendRemoval == "no":
        return

def printJobDetail(user):
    with open('jobfile.txt', 'r') as file:
        data = file.read()
        data_into_list = data.split("\n")    #put value in txt into a list
        print(data_into_list)
        print("\nAll jobs currently in system:")
        for g in range(1,len(data_into_list),6):    #search name of user in that list
            print("Job: " + data_into_list[g])
        

    with open('jobfile_status.txt', 'r') as newfile:
        print("\nJob(s) that you applied/saved in system:")
        data = newfile.read()
        data_into_list = data.split("\n")
        for a in range(len(data_into_list)):    #search name of user in that list
            if data_into_list[a] == user:
                print("User: " + data_into_list[a])
                print("Job title: " + data_into_list[a+1])
                print("Status: " + data_into_list[a+2])
                print("Date grad: " + data_into_list[a+3])
                print("Date start: " + data_into_list[a+4])
                print("Description: " + data_into_list[a+5])

def jobSearch(user, jobDeleted):
    while user: #Keep going until a valid option is put
        if (jobDeleted != 0): #notify if job applied for has been deleted
            with open("jobfile_status.txt", 'r') as file:
                for j in range(len(data_into_list)):
                    if data_into_list[j+1] == 'applied':
                        print("A job(s) that you applied for has been deleted")
                        jobDeleted = 0

        NewJobPost =str(input("\nDo you want to post(p), delete(d) your post or search(s) job/interships: "))
        #POST A JOB
        if NewJobPost == "P" or NewJobPost == "p":
            jobTitle = input("Job title:\n")
            description = input("Description:\n")
            employer = input("Employer:\n")
            location = input("Location\n")
            salary = input("Salary:\n")
            #save data into jobfile.txt
            with open("jobfile.txt", "a") as file:
                file.write(user)            #[i-1]
                file.write("\n")
                file.write(jobTitle)        #[i] search by jobTitle
                file.write("\n")
                file.write(description)     #[i+1]
                file.write("\n")
                file.write(employer)        #[i+2]
                file.write("\n")
                file.write(location)        #[i+3]
                file.write("\n")
                file.write(salary)          #[i+4]
                file.write("\n")
            #Save status of data into jobfile_status.txt at the same time
            with open('jobfile_status.txt', 'a') as filenew:  
                filenew.write(' ')      #use to save user who want to apply or save
                filenew.write("\n")
                filenew.write(jobTitle)      #title [j]
                filenew.write("\n")
                filenew.write(' ')      #STATUS [j+1]
                filenew.write("\n")
                filenew.write(' ')      #grad_date [j+2]
                filenew.write("\n")
                filenew.write(' ')      #start_date [j+3]
                filenew.write("\n")
                filenew.write(' ')      #paragraph [j+4]
                filenew.write("\n")
                
            countJob = 0
            with open(r"jobfile.txt", 'r') as file:  #read each job line save in txt
                countJob = len(file.readlines())
                #print(countJob)
            if countJob > 60:   #6 lines per acc, so 10 accs have 60 lines
                print ("All permitted jobs are created, please come back later")
            break

        #SEARCH A JOB
        elif NewJobPost == "S" or NewJobPost == "s":
            printJobDetail(user)

            with open('jobfile.txt', 'r') as file:
                data = file.read()
                data_into_list = data.split("\n")    #put value in txt into a list
                
                selAJob = str(input("Select the job you want by enter its title ('intership' for example): "))
                for i in range(len(data_into_list)):    #search name of user in that list
                    if data_into_list[i] == selAJob:
                        print("Title: " + data_into_list[i])
                        print("Description: " + data_into_list[i+1])
                        print("Employer: " + data_into_list[i+2])
                        print("Location: " + data_into_list[i+3])
                        print("Salary: " + data_into_list[i+4])

                        aOrS = str(input("Do you want to apply now (a) or (s) save/unsave for later? "))
                        if aOrS == 'a':
                            if data_into_list[i-1] == user: #the user is the one posted
                                print('Cannot apply for a job that you posted')
                            else:
                                with open("jobfile_status.txt", 'r+') as newfile:
                                    data = newfile.read()
                                    #put value in txt into a list
                                    data_into_list = data.split("\n") 
                                    #print(data_into_list)
                                    for j in range(len(data_into_list)):    
                                        #search "title of job" in that list
                                        if (data_into_list[j-1] == user) and (data_into_list[j] == selAJob) and data_into_list[j+1] == 'applied':
                                            print('You applied this job already')
                                            
                                        #if title is in the list (same as selAJob) and "status" is blank or 'saved'
                                        elif (data_into_list[j] == selAJob) and (data_into_list[j+1] == ' ' or data_into_list[j+1] == 'saved'):
                                            grad_date = str(input("Enter grad date (mm/dd/yyyy): "))
                                            start_date = str(input("Enter date start working (mm/dd/yyyy): "))
                                            paragraph = str(input("Enter paragraph answer why you would be a good fit for this job: "))
                                            
                                            with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
                                                data_into_list[j-1] == user
                                                filenew.write(user)             #[j-1]
                                                filenew.write("\n")
                                                filenew.write(selAJob)             #[j]
                                                filenew.write("\n")
                                                filenew.write('applied')        #status stored in here [i+1]
                                                filenew.write("\n")
                                                filenew.write(grad_date)
                                                filenew.write("\n")
                                                filenew.write(start_date)
                                                filenew.write("\n")
                                                filenew.write(paragraph)
                                                filenew.write("\n")
    
                                        else:
                                            pass
                        
                        elif aOrS == 's':
                            if data_into_list[i-1] == user: #the user is the one posted
                                print('Cannot save for a job that you posted')
                            else:
                                with open("jobfile_status.txt", 'r+') as newfile:
                                    data = newfile.read()
                                    #put value in txt into a list
                                    data_into_list = data.split("\n") 
                                    #print(data_into_list)
                                    for j in range(len(data_into_list)):    
                                        #search "title of job" in that list
                                        if (data_into_list[j-1] == user) and (data_into_list[j] == selAJob) and data_into_list[j+1] == 'saved':
                                            sORu = str(input("You saved this post already. Do you want to unsave (u) or keep it (any key): "))
                                            if sORu == 'u': 
                                                print("change status to unsaved")
                                                with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
                                                    data_into_list[j-1] == user
                                                    filenew.write(user)             #[j-1]
                                                    filenew.write("\n")
                                                    filenew.write(selAJob)             #[j]
                                                    filenew.write("\n")
                                                    filenew.write(' ')        #status stored in here [i+1]
                                                    filenew.write("\n")
                                                    filenew.write(" ")
                                                    filenew.write("\n")
                                                    filenew.write(" ")
                                                    filenew.write("\n")
                                                    filenew.write(" ")
                                                    filenew.write("\n")
                                            else:
                                                print("Saved!")
                        
                                        #if title is in the list (same as selAJob) and "status" is blank or 'saved'
                                        elif (data_into_list[j] == selAJob) and (data_into_list[j+1] == ' '):
                                            print("change status to saved")
                                            with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
                                                data_into_list[j-1] == user
                                                filenew.write(user)             #[j-1]
                                                filenew.write("\n")
                                                filenew.write(selAJob)             #[j]
                                                filenew.write("\n")
                                                filenew.write('saved')        #status stored in here [i+1]
                                                filenew.write("\n")
                                                filenew.write(" ")
                                                filenew.write("\n")
                                                filenew.write(" ")
                                                filenew.write("\n")
                                                filenew.write(" ")
                                                filenew.write("\n")
                                        elif (data_into_list[j-1] == user) and (data_into_list[j] == selAJob) and data_into_list[j+1] == 'applied': #new job to save
                                            print("Cannot save a job you posted or applied")
                                        else:
                                            pass
                        
                        else:
                            print("Please select apply(a) or save(s) only.")
                            continue
                            
            break #out of search func
 
        #DELETE A POST
        elif NewJobPost == "D" or NewJobPost == "d":
            print("delete a job that you posted")
            with open('jobfile.txt', 'r') as file:
                print("All jobs currently in system:")
                #jobList = file.readlines()
                #print(jobList)
                data = file.read()
                data_into_list = data.split("\n")    #put value in txt into a list
                print(data_into_list)
                selAJob = str(input("Select the job you want to delete by entering its title: ")) #search in job list
                for i in range(len(data_into_list)):    #search name of user in that list
                    if data_into_list[i] == selAJob:
                        with open('jobfile.txt','w') as file:
                            if data_into_list[i].strip("\n") != selAJob : 
                                file.write(data_into_list[i])
                                print("Job has been deleted!")
                                jobDeleted += 1            
            break

        #EXIT AND RETURN TO GENERAL
        elif NewJobPost == "X" or NewJobPost == "x":
            additionalOptions()
        else:
            print("\nPress (x) to quit\n")




def SearchPeople2():
    userFound = []
    choice = str(input("\n Select a way to search up another user\n"
                        "Press F to search by first name:\n"
                        "Press L to search by last name:\n"
                        "Press C to search by college:\n"
                        "Press M to search by major:\n"))
    if choice == "F" or choice == "f":
        searchFirstName = str(input("\nEnter the first name of the person who you would like to find, or enter R to return\n"))
        if searchFirstName == "R" or searchFirstName == "r":
            return 0
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if searchFirstName.lower()==savedLogin[2].lower():
                x = savedLogin[2] 
                y = savedLogin[3]
                z = x + ' ' + y
                userFound.append(z)
                sendRequest = str(input("Would you like to send them a request?"))
                if sendRequest == "yes":
                    requestSent()
                    return
                if sendRequest == "no":
                    break
    if choice == "L" or choice == "l":
        searchLastName = str(input("\nEnter the last name of the person who you would like to find, or enter R to return\n"))
        if searchLastName == "R" or searchLastName == "r":
            return 0
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if searchLastName.lower()==savedLogin[3].lower():
                x = savedLogin[2] 
                y = savedLogin[3]
                z = x + ' ' + y
                userFound.append(z)
                sendRequest = str(input("Would you like to send them a friend request?"))
                if sendRequest == "yes":
                    requestSent()
                    return
                if sendRequest == "no":
                    break
    if choice == "C" or choice == "c":
        searchCollege = str(input("\nEnter the college of the person who you would like to find, or enter R to return\n"))
        if searchCollege == "R" or searchCollege == "r":
            return 0
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if searchCollege.lower()==savedLogin[4].lower():
                x = savedLogin[2] 
                y = savedLogin[3]
                z = x + ' ' + y
                userFound.append(z)
                sendRequest = str(input("Would you like to send them a friend request?"))
                if sendRequest == "yes":
                    requestSent()
                    return
                if sendRequest == "no":
                    break
    if choice == "M" or choice == "m":
        searchMajor = str(input("\nEnter the major of the person who you would like to find, or enter R to return\n"))
        if searchMajor == "R" or searchMajor == "r":
            return 0
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if searchMajor.lower()==savedLogin[5].lower():
                x = savedLogin[2] 
                y = savedLogin[3]
                z = x + ' ' + y
                userFound.append(z)
                sendRequest = str(input("Would you like to send them a friend request?"))
                if sendRequest == "yes":
                    requestSent()
                    return
                if sendRequest == "no":
                    break
    if len(userFound) == 0:
        print("They are not yet a part of the InCollege system.")

    return userFound


def pending():
    Pending = []
    for name in Request:
        if name == user:
            for pendingName in Request(name):
                Pending.append(pendingName)
    print("\n Here is your list of you pending friend request\n")
    print(Pending)

def friendRequest():
    print("You have a pending friend request")
    requestOption = str(input("Would you like to accept or reject this request?"))
    if requestOption == "accept" or requestOption == "Accept":
        network()
    if requestOption == "reject" or requestOption == "Reject":
        return
    
def requestSent():
    print("Request sent")
    RequestSent=[]
    for name in Request:
        if name == user:
            for requestName in Request(name):
                RequestSent.append(requestName)
                return
    
#messages functions *added in Epic #7*
def sendMessages():
    #Messages file format!!
    #ToUser FromUser Message Read(bool)
    global allUsers

    toUser = str(input("Who would you like to send a message to?"))
    
    #If user is standard, check if toUser is in their friends list
    if userTier == "Standard":
        if toUser in friends:
            message = str(input("What is the message?"))
            messageCount + 1
            with open('messagefile.txt', 'a') as file:
                file.write(user)
                file.write(" to: ")
                file.write(toUser)
                file.write(" Message: ")
                file.write(message)
                file.write("\n")
        else:
            print("User is not your friend!")
        

    #if user is plus, do this:
    else:
        if toUser in allUsers:
            message = str(input("What is the message?"))
            messageCount + 1
            with open('messagefile.txt', 'a') as file:
                file.write("From: ")
                file.write(user)
                file.write(" to: ")
                file.write(toUser)
                file.write(" Message: ")
                file.write(message)
                file.write("\n")
        else: 
            print("User was not found!")


def Messages():
    global user
    if(messageCount > 0):
        with open('messagefile.txt', 'r') as file:
            for line in file: 
                for x in line: #check if user is in messagefile 
                    if user in x: #if user in message file print message
                        print("You have a message:\n")
                        print(line)
                        print("\n")

    if userTier == "Standard":
        sendMessages()
    else:
        global allUsers

        while True:
            viewStudentsList = str(input("Would you like to view all students (y/n)"))
            if viewStudentsList == "y" or viewStudentsList == "Y":
                print(allUsers)
                sendMessages()
                break
            if viewStudentsList == "n" or viewStudentsList == "N":
                sendMessages()
                break
            else:
                print("Invalid input, please try again.")
    
    additionalOptions()



#Pre-login screen
def loginOptions():
    LogOption =str(input("\nDo you have an InCollege account?\n"
                     "Press Y to login or N to create a new account: \n"
                     "Press F to find contacts in InCollege: "))
    while True:
        if LogOption == "Y" or LogOption == "y" or LogOption == "L" or LogOption == "l":
            LogIn()
            break
        if LogOption == "N" or LogOption == "n" or LogOption == "Y" or LogOption == "s":
            CreateAcc()
            break
        if LogOption == "F" or LogOption ==  "f":
            if SearchPeople2():
                LogOption = str(input("\nLog in (L) or sign up (S) to join your friends\n"))
            #loginOptions() #after showing people in contacts, display login options again
         
        else:
            LogOption =str(input("\nDo you have an InCollege account?\n"
                        "Press Y to login or N to create a new account: "))


#CREATE A NEW ACCOUNT
def CreateAcc():
    newUser = str(input('\nPlease enter your new username: '))
    #Support for up to 5 unique student accounts (unique user name)

    #password require: 8 chars min, 12 chars max, at least 1 cap letter, one digit, one special character)
    while True:
        newPass = str(input("\n\n*** Your password must have: *** \n"
                        "+ Minimum of 8 characters\n"
                        "+ Maximum of 12 characters\n"
                        "+ At least one capital letter, one digit, one special character\n"
                        "\nEnter your new password: "))
        upper = any(ele.isupper() for ele in newPass)           #at least 1 cap letter
        digit = any(e.isdigit() for e in newPass)               #at least 1 digit
        specChar = any(not c.isalnum() and 
                    not c.isspace() for c in newPass)        #at least 1 special char

        if len(newPass)>7 and len(newPass)<13 and upper and digit and specChar:   
            #after username and password are valid, ask for first and last name, and store new user password, first name, and last name in file          
            firstName = str(input("\nPlease enter your first name \n"))
            lastName = str(input("\nPlease enter your last name\n"))
            College = str(input("\nPlease enter the college you attend \n"))
            major = str(input("\nPlease enter your major\n"))
            tier = str(input("\nDo you want a Standard account (free) or Plus account ($10/month)")) #added tier epic7
            if(tier == "Plus" or tier == "plus"):
                tier = "Plus"
                print("Awesome! You will be billed $10/month")
            elif tier == "Standard" or tier == "standard":
                tier = "Standard"


            file = open("userfile.txt", "a")
            file.write(newUser)
            file.write(" ")
            file.write(newPass)
            file.write(" ")
            file.write(firstName)
            file.write(" ")
            file.write(lastName)
            file.write(" ")
            file.write(College)
            file.write(" ")
            file.write(major)
            file.write(" ")
            file.write(tier)    #Save tier info to user file *added in Epic #7*
            file.write("\n")

            countAcc = 0
            with open("userfile.txt", 'r') as file:  #read each account line save in txt
                countAcc = len(file.readlines())
                #print(countAcc)

            if countAcc > 10:
                print ("All permitted accounts are created, please come back later")
                break
            file.close

            settingsFile = open("usersettings.txt", "a")
            settingsFile.write(newUser)
            settingsFile.write(" ")
            settingsFile.write("On")        #InCollege Email
            settingsFile.write(" ")
            settingsFile.write("On")        #SMS
            settingsFile.write(" ")
            settingsFile.write("On")        #Targeted Advertising
            settingsFile.write(" ")
            settingsFile.write("English")   #Language
            settingsFile.write(" ")
            settingsFile.write("\n")

            settingsFile.close()

            allUsersFile = open("allUsers.txt", "a")
            allUsersFile.write(newUser)
            allUsersFile.write("\n")
            allUsersFile.close()
            allUsers.append(newUser)

            print('\nCongrats! You are successfully sign up.' 
                    '\nYou can login now...')


            #call login function
            LogIn()
            break


#LOGIN WITH AN ACCOUNT
def LogIn():
    global user
    global userTier
    while True:
        username = str(input("\nPlease enter your username: "))
        password = str(input("\nPlease enter your password: "))

        # login success system will tell them "You have successfully logged in"
        # "Incorrect username / password, please try again". Allow attempt to log in again and unlimited # of log in.

        #read textfile and check if they are equal
        for line in open("userfile.txt", "r").readlines():
            savedLogin = line.split() #stores results in a list of two strings and splits on the space
            if username==savedLogin[0] and password==savedLogin[1]:
                print("\n*** You have successfully logged in! ***")
                user = username
                userTier = savedLogin[6]    #Save user's tier to a global variable when they log in *added in Epic #7*
                additionalOptions()
                return

        print("\n*** Incorrect username/password, please try again. ***")

def WatchVideo():
    print("Video is now playing...")
    
def General():
    generalInput = str(input("\nSign up\n" "Help Center\n" "About\n" "Press\n" "Blog\n" "Careers\n" "Developers\n" "Go Back\n"))
    if generalInput == "Sign up" or "s":
        loginOptions()
    if generalInput == "Help Center":
        print("\nWe're here to help.\n")
    if generalInput == "About":
        print("\nInCollege: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide\n")
    if generalInput == "Press":
        print("\nInCollege Pressroom: Stay on top of the latest news, updates, and reports\n")
    if generalInput == "Blog":
        print("\nUnder construction\n")
    if generalInput == "Careers":
        print("\nUnder construction\n")
    if generalInput == "Developers":
        print("\nUnder construction\n")
    if generalInput == "Go Back":
        print("Returning... \n")
        return

def UsefulLinks():
    usefulLinksInput = str(input("\n\nPlease enter where you would like to go:\n" "General\n" "Browse InCollege\n" "Business Solutions\n" "Directories \n" "Go Back\n"))
    if usefulLinksInput == "General" or "g":
        General()
    if usefulLinksInput == "Browse InCollege":
        print("\nUnder construction\n")
    if usefulLinksInput == "Business Solutions":
        print("\nUnder construction\n")
    if usefulLinksInput == "Directories":
        print("\nUnder construction\n")
    if usefulLinksInput == "Go Back":
        print("Returning...\n")
        return                      #Return to previous location

def ImportantLinks():
    while True: 
        importantLinksInput = str(input("Please enter where you would like to go:\n" "A Copyright Notice\n" "About Accessibility\n" "User Agreement\n" "Privacy Policy\n" "Cookie Policy\n" "Copyright Policy\n" "Brand Policy\n" "Guest Controls\n" "Languages\n" "Go back\n"))
        if importantLinksInput == "A Copyright Notice":
            print("Copywright 2022 InCollege inc. All rights reserved")
        elif importantLinksInput == "About":
            print("InCollege is a fast-growing application dedicated to bringing useful tools for college students around the world. Our goal is to assist college students in being as successful as possible.")
        elif importantLinksInput == "Accessibility":
            print("InCollege is committed to providing a website that is accessible to the widest possible audience, regardless of technology or ability. We are actively working to increase the usability and accessibility of InCollege and in doing so adhere to many of the available standards and guidelines.")
        elif importantLinksInput == "User Agreement":
            print("Welcome and thank you for using InCollege! When using this application, you are agreeing to our terms, so please take a few minutes to read over the user agreement below.\n" "InCollege is licensed to you(end-user) by InCollege inc., located at 4202 E Fowler Ave. Tampa, FL, 33612, United States (Licensor), for use only under the terms of thus license agreement. Our VAT number is SE99999911999. By downloading the Licensed Application from Apple and Google's software distribution platforms, you indicate that you agree to be bound by all the terms and conditions of this license agreement. ")
        elif importantLinksInput == "Privacy Policy":
            print("At InCollege, our fundamental philosophy is 'student's first.' That value power's all of the decisions we make, including how we gather and respect your personal information. Below we have created a policy as clear as possible so our member's can be informed.\n " "We will only collect the required information fro our users through the InCollege application in order to better understand our users. Information will be collected through cookies and other tracking technologies and will only be shared within InColleg inc. Users have special rughts over their data and can choose what they wish to share with our team. You may contact us at incollege@incollege.net for any questions or concerns.")
            GuestControls()
        elif importantLinksInput == "Cookie Policy":
            print("At InCollege, we believe in being clear and open about how we use your information. In the spirit of transparency, this policy provides detailed information about how and when we use cookies.\n" "Cookies are files created by websites you may visit and our company uses cookies in orer to provide the best possible user experience. There are first-party cookies, session cookies, third-party cookies, persistent cookies, and secure cookies. InCollege will only use the necessary cookies in order to better understand our users and you can manage the use of your cookies at the bottom of your screen.")
        elif importantLinksInput == "Copyright Policy":
            print("You may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to others without obtaining the prior written consent of the owner of such proprietary rights. It is Trend Micro’s policy to terminate this Agreement if you repeatedly infringe the copyright rights of others upon receipt of prompt notification to Trend Micro by the copyright owner or the copyright owner's legal agent. Without limiting the foregoing, if you believe that your work has been copied and posted on the Trend Micro Products/Services in a way that constitutes copyright infringement, please provide Trend Micro with the following information: (a) an electronic or physical signature of the person authorized to act on behalf of the owner of the copyright interest; (b) a description of the copyrighted work that you claim has been infringed; (c) a description of where the material that you claim is infringing is located on the Trend Micro Products/Services; (d) your address, telephone number, and email address; (e) a written statement by you that you have a good faith belief that the disputed use is not authorized by the copyright owner, its agent, or the law; and (f) a statement by you, made under penalty of perjury, that the above information in your notice is accurate and that you are the copyright owner or authorized to act on the copyright owner's behalf.")
        elif importantLinksInput == "Brand Policy":
            print("The InCollege brand is to put student's first. Any use or mention of the brand should keep the company's main goal in mind and be sure to properly represent InCollege.")
        elif importantLinksInput == "Go Back":
            print("Returning...\n")
            break


def GuestControls():
    while user:     #while user has a value, aka the user is logged in
        print("Your current settings are:\n")
        lines = open("usersettings.txt", "r").readlines()
        updatedLines = []
        for line in lines:      #search for the user in the settings file
            splitLine = line.split()
            if user == splitLine[0]:     
                print("InCollege Email: ", splitLine[1], "\n",
                      "SMS: ", splitLine[2], "\n",
                      "Targeted Advertising: ", splitLine[3], "\n",
                      "Language: ", splitLine[4], "\n")
                changeSetting = str(input("Which setting would you like to change? or enter None for none\n"))
                if changeSetting == "None":
                    return
                else:
                    if changeSetting == "InCollege Email":
                        if splitLine[1] == "On":
                            splitLine[1] = "Off"
                        else:
                            splitLine[1] = "On"
                    if changeSetting == "SMS":
                        if splitLine[2] == "On":
                            splitLine[2] = "Off"
                        else:
                            splitLine[2] = "On"
                    if changeSetting == "Targeting Advertising":
                        if splitLine[3] == "On":
                            splitLine[3] = "Off"
                        else:
                            splitLine[3] = "On"
                    if changeSetting == "Language":
                        if splitLine[4] == "On":
                            splitLine[4] = "Off"
                        else:
                            splitLine[4] = "On"
                line = splitLine[0] + " " + splitLine[1] + " " + splitLine[2] + " " + splitLine[3] + " " + splitLine[4] + "\n"
                updatedLines.append(line)
        out = open("usersettings.txt", 'w')
        out.writelines(updatedLines)
        out.close()
        break

    #if the user isn't logged in:
    print("You are not signed in")




#THIS MUST BE MAIN FUNC
#Using existing InCollege account or Creating a new account
def main():
    UserStory = print("\n\nWelcome to InCollege! InCollege is a website to help college students make connections and get jobs. Don't believe us? Take it from our users! \n\"I was a senior about to graduate without a job, but with the help of InCollege, I got a job and am now a very successful person\" -John Doe")
    VideoOption = str(input("Want to see more on how InCollege has brightened the future of college students? Watch this video! (Y/N)"))
    if VideoOption == "Y" or VideoOption == "y":
        WatchVideo()

    while(True):
        links = str(input("\nWould you like to view Useful Links(U) or InCollege Important Links(I):\n"))
        if links == "U" or "u":
            UsefulLinks()
        elif links == "I" or "i":
            ImportantLinks()
        else:
            print("Invald input, please press U or I to choose:")
            continue

if __name__ == "__main__":
    main()

#call prelogin screen
#loginOptions()
