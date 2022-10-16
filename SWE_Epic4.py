#Epic 4

#Global Variables

user = "" 




#AFTER LOGIN = HOME PAGE
#created a function in order to call it again when asked to return to the main screen
def additionalOptions():
    global user
    addiOption = str(input("\nPress J to search for a job:\n"
                        "Press F to find someone you know:\n"
                        "Press S to learn a new skill:\n"
                        "Press N to see your network:\n"
                        "Press P to see pending friend requests: \n"
                        "Or, enter InCollege Important Links to view important InCollege links\n"))
    if addiOption == "J" or addiOption == "j":
        jobSearch(user)

    if addiOption == "F" or addiOption == "f":
        SearchPeople()

    #after selecting learn new skill, present 5 skills for user to select or return
    if addiOption == "S" or addiOption == "s":
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
    if addiOption == "N" or addiOption == "n":
        network(user)
    if addiOption == "P" or addiOption == "p":
        friendRequest()
    if addiOption == "InCollege Important Links":
        ImportantLinks()

def network(user):
    friends =[] #friends list initially empty
    friend = str(input("How would you like your new friend's name stored in your friend's list?"))
    friends.append(friend)
    viewList = str(input("Would you like to see your network"))
    if viewList == "Yes" or viewList == "yes":
        print(friends)
    if viewList == "No" or viewList == "no":
        return
    friendRemoval = str(input("Would you like to remove a friend?"))
    if friendRemoval == "yes":
        remove = str(input("Who would you like to remove?"))
        friends.remove(remove)
    if friendRemoval == "no":
        return

def jobSearch(user):
    #Ask user if they want to add a job or return
    NewJobPost =str(input("\nPost a job or return? (y/n/r)\n"))
    while True: #Keep going until a valid option is put
        if NewJobPost == "Y" or NewJobPost == "y":
            jobTitle = input("Job title:\n")
            description = input("Description:\n")
            employer = input("Employer:\n")
            location = input("Location\n")
            salary = input("Salary:\n")

            file = open("jobfile.txt", "a")
            file.write(user)
            file.write(" ")
            file.write(jobTitle)
            file.write(" ")
            file.write(description)
            file.write(" ")
            file.write(employer)
            file.write(" ")
            file.write(location)
            file.write(" ")
            file.write(salary)
            file.write("\n")
            

            countJob = 0
            with open(r"jobfile.txt", 'r') as file:  #read each job line save in txt
                countJob = len(file.readlines())
                #print(countAcc)

            if countJob > 5:
                print ("All permitted jobs are created, please come back later")
            file.close
            break
        elif NewJobPost == "R" or NewJobPost == "r":
            additionalOptions()
        elif NewJobPost == "N" or NewJobPost == "n":
            break
        else:  
            NewJobPost =str(input("Invalid option, please try again. (y/n/r)"))

"""
def SearchPeople():
    userFound = False
    searchFirstName = str(input("\nEnter the first name of the person who you would like to find, or enter R to return\n"))
    if searchFirstName == "R" or searchFirstName == "r":
        return 0
    searchLastName = str(input("\nEnter the last name of the person you would like to find\n"))
    for line in open("userfile.txt", "r").readlines():
        savedLogin = line.split() #stores results in a list of two strings and splits on the space
        if searchFirstName.lower()==savedLogin[2].lower() and searchLastName.lower()==savedLogin[3].lower():
            userFound = True
            print("They are Part of the InCollege System.")
            break

    if userFound == False:
        print("They are not yet a part of the InCollege system.")

    return userFound
"""

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
                break
    if len(userFound) == 0:
        print("They are not yet a part of the InCollege system.")

    return userFound

def friendRequest():
    print(“You have a pending friend request”)
    requestOption = str(input(“Would you like to accept or reject this request?”))
    if requestOption == "accept" or requestOption == "Accept":
        network()
    if requestOption == "reject" or requestOption == "Reject":
        return
    

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
            if SearchPeople():
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
            file.write("\n")

            countAcc = 0
            with open(r"userfile.txt", 'r') as file:  #read each account line save in txt
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

            print('\nCongrats! You are successfully sign up.' 
                    '\nYou can login now...')

            #call login function
            LogIn()
            break
    
#The 6th attempt to create a student account will result in the message "All permitted accounts have been created, please come back later"

#LOGIN WITH AN ACCOUNT
def LogIn():
    global user
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
                additionalOptions()
                return

        print("\n*** Incorrect username/password, please try again. ***")

def WatchVideo():
    print("Video is now playing...")
    
def General():
    generalInput = str(input("Sign up\n" "Help Center\n" "About\n" "Press\n" "Blog\n" "Careers\n" "Developers\n" "Go Back\n"))
    if generalInput == "Sign up":
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
    usefulLinksInput = str(input("Please enter where you would like to go:\n" "General\n" "Browse InCollege\n" "Business Solutions\n" "Directories \n" "Go Back\n"))
    if usefulLinksInput == "General":
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
    UserStory = print("Welcome to InCollege! InCollege is a website to help college students make connections and get jobs. Don't believe us? Take it from our users! \n\"I was a senior about to graduate without a job, but with the help of InCollege, I got a job and am now a very successful person\" -John Doe")
    VideoOption = str(input("Want to see more on how InCollege has brightened the future of college students? Watch this video! (Y/N)"))
    if VideoOption == "Y" or VideoOption == "y":
        WatchVideo()

    while(True):
        links = str(input("Would you like to view Useful Links or InCollege Important Links:\n"))
        if links == "Useful Links":
            UsefulLinks()
        elif links == "InCollege Important Links":
            ImportantLinks()
        else:
            print("Invald input, please try again")
            continue

if __name__ == "__main__":
    main()


#call prelogin screen
#loginOptions()
