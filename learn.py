import csv  #https://www.youtube.com/watch?v=q5uM4VKywbA

with open('names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line)     #print all line with it title 'email': toanho@yahoo.com
        #print(line['email'])    #print all email only (column)
        if line['first_name'] == 'Toan':
            print(line['first_name'])
            print(line['last_name'])
            print(line['email'])
            
    
    
    # next(csv_reader) #skip the first row

    # for line in csv_reader:
    #     #print(line) #print all line rows and column
    #     print(line[2])  #print only email column

    # use dash as delimiter
with open('new_names.csv', 'w') as new_file:
    fieldnames = ['first_name', 'last_name', 'email']

    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t') #use dash as delimiter
    # csv_writer = csv.writer(new_file, delimiter='\t') #use dash as delimiter

    csv_writer.writeheader()

    for line in csv_reader: #we write each line of the original names.csv
        csv_writer.writerow(line) #to new_names.csv

    