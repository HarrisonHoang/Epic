


while True: #Keep going until a valid option is put
    user = "toan"

    NewJobPost =str(input("\nDo you want to post(p), delete(d) your post or search(s) job/interships: "))

    if NewJobPost == "P" or NewJobPost == "p":
        jobTitle = input("Job title:\n")
        description = input("Description:\n")
        employer = input("Employer:\n")
        location = input("Location\n")
        salary = input("Salary:\n")

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
            
            countJob = 0
            with open(r"jobfile.txt", 'r') as file:  #read each job line save in txt
                countJob = len(file.readlines())
                #print(countAcc)
            if countJob > 10:
                print ("All permitted jobs are created, please come back later")
        break


    elif NewJobPost == "S" or "s":
        print("All jobs currently in system:")

        with open('jobfile.txt', 'r') as file:
            #jobList = file.readlines()
            #print(jobList)
            data = file.read()
            data_into_list = data.split("\n")       #put value in txt into a list
            print(data_into_list)
            for i in range(len(data_into_list)):    #search name of user in that list
                if data_into_list[i] == user:
                    print(data_into_list[i])
                    print(data_into_list[i+1])
                    print(data_into_list[i+2])
                    print(data_into_list[i+3])
                    print(data_into_list[i+4])
                    print(data_into_list[i+5])

            
        break



    elif NewJobPost == "D" or "d":
        print("delete a job that you posted")
        break


    elif NewJobPost == "X" or NewJobPost == "x":
        #additionalOptions()
        break
    else:
        print("\nPress (x) to quit\n")
        break