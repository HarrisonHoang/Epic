def printJobDetail(user):
    with open('jobfile.txt', 'r') as file:
        print("\nAll jobs currently in system:")
        data = file.read()
        data_into_list = data.split("\n")    #put value in txt into a list
        for g in range(1,len(data_into_list),6):    #search name of user in that list
            print("Job: " + data_into_list[g])
        
        print(data_into_list)

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


while True: #Keep going until a valid option is put
    user = "hays"

    NewJobPost =str(input("\nDo you want to post(p), delete(d) your post or search(s) job/interships: "))

    if NewJobPost == "P" or NewJobPost == "p": 
        jobTitle = input("Job title:\n")
        description = input("Description:\n")
        employer = input("Employer:\n")
        location = input("Location\n")
        salary = input("Salary:\n")
        status = " "
        #file = open("jobfile.txt", "a")
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

        with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
            filenew.write(' ')      #use to save user who want to apply or save
            filenew.write("\n")
            filenew.write(jobTitle)      #title [j]
            filenew.write("\n")
            filenew.write(' ')      #status stored in here [j+1]
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
            if countJob > 60:
                print ("All permitted jobs are created, please come back later")
        break
    



    elif NewJobPost == "S" or NewJobPost == "s":
        printJobDetail(user)

        with open('jobfile.txt', 'r') as file:
            data = file.read()
            data_into_list = data.split("\n")
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
                                    if (data_into_list[j-1] == user) and (data_into_list[j] == selAJob) and (data_into_list[j+1] == 'applied'):
                                        print('You applied this job already')
                                        
                                    #if title is in the list (same as selAJob) and "status" is blank or 'saved'
                                    if (data_into_list[j] == selAJob) and (data_into_list[j+1] == ' ' or data_into_list[j+1] == 'saved'):
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
                                            print("Change status to unsaved")
                                            with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
                                                data_into_list[j-1] == user
                                                filenew.write(user)             #[j-1]
                                                filenew.write("\n")
                                                filenew.write(selAJob)             #[j]
                                                filenew.write("\n")
                                                filenew.write(' ')        #status stored in here [i+1]
                                                filenew.write("\n")
                                        else:
                                            print("Saved!")
                    
                                    #if title is in the list (same as selAJob) and "status" is blank or 'saved'
                                    elif (data_into_list[j] == selAJob) and (data_into_list[j+1] == ' '):
                                        print("Change status to saved")
                                        with open('jobfile_status.txt', 'a') as filenew:   #read/write to "apply or save jobfile"
                                            data_into_list[j-1] == user
                                            filenew.write(user)             #[j-1]
                                            filenew.write("\n")
                                            filenew.write(selAJob)          #[j]
                                            filenew.write("\n")
                                            filenew.write('saved')        #status stored in here [i+1]
                                            filenew.write("\n")
                                    elif (data_into_list[j-1] == user) and (data_into_list[j] == selAJob) and data_into_list[j+1] == 'applied': #new job to save
                                        print("Cannot save a job you posted or applied")
                                    else:
                                        print(" ")
                    
                    else:
                        print("Please select apply(a) or save(s) only.")
                        continue
                         
        break #out of search func







    elif NewJobPost == "D" or NewJobPost == "d":
        print("delete a job that you posted")
        printJobDetail()
        break


    elif NewJobPost == "X" or NewJobPost == "x":
        #additionalOptions()
        break
    else:
        print("\nPress (x) to quit\n")
