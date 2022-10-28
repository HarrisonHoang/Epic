


while True: #Keep going until a valid option is put
    user = "toan"

    NewJobPost =str(input("\nDo you want to post(p), delete(d) your post or search(s) job/interships: "))

    if NewJobPost == "P" or NewJobPost == "p":
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
        if countJob > 10:
            print ("All permitted jobs are created, please come back later")
        file.close
        break


    elif NewJobPost == "S" or "s":
        print("All jobs currently in system:")
        f = open(r'jobfile.txt', 'r')
        content = f.read()
        f.close()



    elif NewJobPost == "D" or "d":
        print("delete a job that you posted")
        


    elif NewJobPost == "X" or NewJobPost == "x":
        #additionalOptions()
        break
    else:
        print("\nPress (x) to quit\n")
        break