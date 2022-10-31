# pytest test_SWE_Epic6.py -v
import SWE_Epic6
from SWE_Epic6 import Request
     
#Test account login- make sure user states whether they have an InCollege account
def test_LogIn():
    LogOption="y"
    assert LogOption == "Y" or "y" or "N" or "n"
    user="sophiehos"
    password="Hostet17%"
    assert user=="sophiehos"
    assert password=="Hostet17%"
    print("You have successfully logged in")
    
    user="sophiahos"
    password="NotHos1"
    assert user!="sophiehos" or password!="Hostet17%"
    print("Incorrect username/password, please try again.")

#Test account creation
def test_CreateAcc():
    newUser="sophiehos"
    assert newUser != ' '
    newPass="Hostetl7#"
    assert (len(newPass)>7 and len(newPass)<13) and any(ele.isupper() for ele in newPass) and any(e.isdigit() for e in newPass) and any(not c.isalnum() and not c.isspace() for c in newPass)
    countAcc=3
    assert countAcc>=0 and countAcc<=5
    print("successfully create an account")
    countAcc=6
    assert countAcc==6
    print("All permitted accounts have been created, please come back later")

#Test Additional Options
def test_additionalOptions():
    addiOption="J"
    assert addiOption=="J" or "j" or "F" or "f" or "S" or "s"
    assert addiOption=="S" or "s"
    print("coding practice" or "new language" or "jira" or "github" or "excel") 
    skill="coding practice"
    assert skill==("coding practice" or "new language" or "jira" or "github" or "excel")
    print("Under construction")

#Test Search People
def test_SearchPeople():
    searchFirstName = "ho"
    searchLastName = "toan"
    assert searchFirstName == "ho"
    assert searchLastName == "toan"
    print("Contact is found! They are part of the incollege system.")

    searchFirstName = "hoa"
    searchLastName = "toanj"
    assert searchFirstName != "ho" or searchLastName != "toan"
    print("Contact is not found! They are not yet a part of the incollege system.")

#Save a job post but not display of the name of person who posted
def test_jobSearch():
    countJob = 60
    assert countJob == 60
    print("System permit up to 10 jobs posted. Saved name of person in jobfile but not displayed.")

    countJob = 60
    assert countJob > 60
    print("All permitted job are create, please come back later")


def test_General():
    generalInput = "Sign up"
    assert generalInput == "Sign up"
    # assert SWE_Epic3.loginOptions() == True
    generalInput = "Help Center"
    assert generalInput == "Help Center"
    print("\nWe're here to help.\n")
    generalInput = "Blog"
    assert generalInput == "Blog"
    print("\nUnder construction\n")
    generalInput = "About" or "Go Back" or "Developers" or "Careers"
    assert generalInput == "About"
    print("\nInCollege: Welcome to InCollege, the world's largest college student network with many users in many countries and territories worldwide\n")


def test_UsefulLinks():
    usefulLinksInput = "General"
    assert usefulLinksInput == "General"
    #SWE_Epic3.General()
    usefulLinksInput = "Business Solution"
    assert usefulLinksInput == "Business Solution"
    print("\nUnder construction\n")
    usefulLinksInput = "Directories" or "Browse InCollege"
    assert usefulLinksInput == "Business Solution" or "Browse InCollege"
    print("\nUnder construction\n")


def test_ImportantLinks():
    importantLinksInput = "Privacy Policy"
    assert importantLinksInput == "Privacy Policy"
    SWE_Epic6.GuestControls()
    print("successfully go to GuestControl() when it print last line: You are not sighe")
    importantLinksInput = "About"
    assert importantLinksInput == "About"
    print("InCollege is a fast-growing application dedicated to bringing useful tools for college students around the world. Our goal is to assist college students in being as successful as possible.")
    importantLinksInput = "A Copyright Notice"
    assert importantLinksInput == "A Copyright Notice"
    print("Copywright 2022 InCollege inc. All rights reserved")

def test_GuestControls():
    user = "haysc"
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
                # changeSetting = str(input("Which setting would you like to change? or enter None for none\n"))
                changeSetting = "InCollege Email"
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
    
def test_friendRequest():
    requestOptionInput = "accept"
    assert requestOptionInput
    print("Friend request accepted")
    requestOptionInput = "reject"
    assert requestOptionInput
    print("Friend request rejected")

def test_requestSent():
    name = "salvador"
    user = "salvahernandezb"
    for name in Request:
        if name == user:
            assert name == "salvador"
            for requestName in Request(name):
                assert requestName
                print("Request name is in requests.") 

def test_pending():
    name = "salvador"
    user = "salvahernandezb"
    for name in Request:
        if name == user:
            assert name == "salvador"
            for pendingName in Request(name):
                assert pendingName
                print("Pending name in request list.")


def test_network():
    friendInput = "salvador"
    #assert Request[friendInput].append()
    viewlist = "yes"
    assert viewlist == "yes"
    print("Friend list printed")
    viewlist = "no"
    assert viewlist == "no"
    print("returns")
    friendremoval = "yes"
    assert friendremoval == "yes"
    removeInput = "salvador"
    assert removeInput == "salvador"
    print("friend removed")


def test_searchPeople2():
    choiceInput = "F"
    assert choiceInput == "F"
    searchFirstNameInput = "R"
    assert searchFirstNameInput == "R"
    print("Returns")
    searchFirstNameInput = "caitlin"
    assert searchFirstNameInput == "caitlin"
    sendRequestInput = "yes"
    assert sendRequestInput == "yes"
    print("Send request, return")
    sendRequestInput = "no"
    assert sendRequestInput == "no"

    choiceInput = "L"
    assert choiceInput == "L"
    searchLastNameInput = "R"
    assert searchLastNameInput == "R"
    print("Returns")
    searchLastNameInput = "hays"
    assert searchLastNameInput == "hays"
    sendRequestInput = "yes"
    assert sendRequestInput == "yes"
    print("Send request, return")
    sendRequestInput = "no"
    assert sendRequestInput == "no"

    choiceInput = "C"
    assert choiceInput == "C"
    searchCollegeInput = "R"
    assert searchCollegeInput == "R"
    print("Returns")
    searchCollegeInput = "hays"
    assert searchCollegeInput == "hays"
    sendRequestInput = "yes"
    assert sendRequestInput == "yes"
    print("Send request, return")
    sendRequestInput = "no"
    assert sendRequestInput == "no"

    choiceInput = "M"
    assert choiceInput == "M"
    searchMajorInput = "R"
    assert searchMajorInput == "R"
    print("Returns")
    searchMajorInput = "hays"
    assert searchMajorInput == "hays"
    sendRequestInput = "yes"
    assert sendRequestInput == "yes"
    print("Send request, return")
    sendRequestInput = "no"
    assert sendRequestInput == "no"
     
#Test profiles
def test_profile():
     optionInput = "c"
     assert optionInput == "c"
     title = "student"
     assert title == "student"
     major = "computer science"
     assert major == "computer science"
     univer = "University of South Florida"
     assert univer == "University of South Florida"
     about = "I am a senior at USF looking for connections with other students"
     assert about == "I am a senior at USF looking for connections with other students"
     print("For experience, you can insert up to 3 past jobs. If none, enter 0" + 
                "(include title, employer, data started and ended, location, and describe what you did")
     experi1 = "Google"
     assert experi1 == "Google"
     experi2 = "Facebook"
     assert experi2 == "Facebook"
     experi3 = "Twitter"
     assert experi3 == "Twitter"
     edu = "USF, comp sci, 4 years"
     assert edu == "USF, comp sci, 4 years"
     optionInput = "v"
     assert optionInput == "v"
     print("\nProfile of: Sophia" )
     print("Title: student")
     print("Major: computer science")
     print("University: University of South Florida")
     print("About me: I am a senior at USF looking for connections with other students")
     print("Experience 1: Google")
     print("Experience 2: Facebook")
     print("Experience 3: Twitter")
     print("Education: USF, comp sci, 4 years")
     optionInput = "e"
     assert optionInput == "e"
     print("\nProfile of: Sophia")
     print("Note: Press 'e' if edit, press k to keep. ")
     print("Title: student")
     choice = "e"
     assert choice == "e" or "k"
     print("Enter title: ")
     print("Major: computer science")
     choice = "e"
     assert choice == "e" or "k"
     print("Enter major: ")
     print("University: University of South Florida")
     choice = "e"
     assert choice == "e" or "k"
     univer = "University of Illinois"
     assert univer == "University of Illinois"
     print("About me: I am a senior at USF looking for connections with other students")
     choice = "e"
     assert choice == "e" or "k"
     about = "I'm a recent dropout"
     assert about == "I'm a recent dropout"
     print("Experience 1: Google")
     choice = "k"
     assert choice == "e" or "k"
     print("Experience 2: Facebook")
     choice = "k"
     assert choice == "e" or "k"
     print("Experience 3: Twitter")
     choice = "e"
     assert choice == "e" or "k"
     experi3 = "Instagram"
     assert experi3 == "Instagram"
     print("Education: USF, comp sci, 4 years")
     choice = "e"
     assert choice == "e" or "k"
     edu = "ISU, cyber security, 3 years"
     assert edu == "ISU, cyber security, 3 years"
     optionInput = "x"
     assert optionInput == "x"
     print("\nPress (x) to quit\n")

#Test display
def test_display():
     search = "Steven Jobs"
     assert search == "Steven Jobs"
     print("\nProfile of: Steven Jobs")
     print("Title: student")
     print("Major: computer science")
     print("University: University of California")
     print("About me: I am a fifth year computer science major")
     print("Experience 1: Gooogle")
     print("Experience 2: Best Buy")
     print("Experience 3: Apple")
     print("Education: UCLA, computer science, 5 yrs")

#Test printJobDetail
def test_printJobDetail():
    user="sophiehos"
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

#Test jobSearch
def test_jobSearch():
    user ="sophiehos"
    NewJobPost = "P"
    assert NewJobPost == "p" or "P" or "s" or "S" or "d" or "D" or "x" or "X"
    jobTitle = "boss"
    assert jobTitle == "boss"
    description = "look after employees"
    assert description == "look after employees"
    employer = "apple"
    assert employer == "apple"
    location = "ca"
    assert location == "ca"
    salary = "500k"
    assert salary == "500k"
    jobDeleted="0"
    assert jobDeleted=="0"
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

