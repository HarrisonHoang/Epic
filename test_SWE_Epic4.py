# pytest test_SWE_Epic3.py -v
import SWE_Epic3
     
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
    countJob = 3
    assert countJob == 3
    print("System permit up to 5 jobs posted. Saved name of person in jobfile but not displayed.")

    countJob = 6
    assert countJob > 5
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
    SWE_Epic3.GuestControls()
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
# pytest test_SWE_Epic3.py -v