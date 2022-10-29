def printJobDetail():
    with open('jobfile.txt', 'r') as file:
            #jobList = file.readlines()
            #print(jobList)
            data = file.read()
            data_into_list = data.split("\n")       #put value in txt into a list
            #print(data_into_list)
            for i in range(len(data_into_list)):    #search name of user in that list
                if data_into_list[i] == user:
                    print(data_into_list[i])
                    print(data_into_list[i+1])
                    print(data_into_list[i+2])
                    print(data_into_list[i+3])
                    print(data_into_list[i+4])
                    print(data_into_list[i+5])


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
            file.write(user)
            file.write("\n")
            file.write(jobTitle)
            file.write("\n")
            file.write(description)
            file.write("\n")
            file.write(employer)
            file.write("\n")
            file.write(location)
            file.write("\n")
            file.write(salary)
            file.write("\n")
            file.write(status)  #auto status = blank
            file.write("\n")
            
            countJob = 0
            with open(r"jobfile.txt", 'r') as file:  #read each job line save in txt
                countJob = len(file.readlines())
                #print(countAcc)
            if countJob > 10:
                print ("All permitted jobs are created, please come back later")
        break


    elif NewJobPost == "S" or "s":

        with open('jobfile.txt', 'r') as file:
            #jobList = file.readlines()
            #print(jobList)
            data = file.read()
            data_into_list = data.split("\n")       #put value in txt into a list
            print("All jobs currently in system:")
            print(data_into_list)
            
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
                        if data_into_list[i+5] == ' ':
                            grad_date = str(input("Enter grad date (mm/dd/yyyy): "))
                            start_date = str(input("Enter date start working (mm/dd/yyyy): "))
                            paragraph = str(input("Enter paragraph answer why you would be a good fit for this job: "))
                            #with open('jobfile.txt', 'w') as file:
                                #data_into_list[i+5] = 'applied'     #change status to 'applied'
                                #file.write
                                #print(data_into_list[i+5])
                        if data_into_list[i+5] == 'applied':
                            print('You applied this already')
                    
                    if aOrS == 's':
                        if data_into_list[i+5] == 'saved': #saved already
                            sORu = str(input("You saved this post already. Do you want to unsave (u) or keep it (any key): "))
                            if sORu == 'u': 
                                print("change status to saved")
                                ##with open('jobfile.txt', 'w') as file:
                                    #data_into_list[i+5] = 'saved'     #change status to 'applied'
                                    #file.write
                                    #print(data_into_list[i+5])
                            else:
                                print("Saved!")
                        if data_into_list[i+5] == ' ': #new job to save
                            print("change status to saved")
                            ##with open('jobfile.txt', 'w') as file:
                                #data_into_list[i+5] = 'saved'     #change status to 'applied'
                                #file.write
                                #print(data_into_list[i+5])
                        if data_into_list[i+5] == 'applied' or data_into_list[i-1] == user: #new job to save
                            print("Cannot save a job you posted or applied")
                        
                        


            
        break



    elif NewJobPost == "D" or "d":
        print("delete a job that you posted")
        printJobDetail()
        break


    elif NewJobPost == "X" or NewJobPost == "x":
        #additionalOptions()
        break
    else:
        print("\nPress (x) to quit\n")
        break

