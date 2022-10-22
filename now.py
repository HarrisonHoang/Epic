import csv
ACCEPTED_MSG = """
Hi {},

We are thrilled to let you know that you are accepted to our program workshop.
"""

#field names
fields = ['Name', 'Major', 'Year', 'CGPA']

#data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']]

# #name of csv file
# filename = "now.csv"

#writing to csv file
with open(filename, 'w') as s:
    #creating a csv writing object
    c = csv.writer(s)

    #writing the fields
    c.writerow(fields)

    #writing the data rows
    c.writerows(rows)


#with opening the csv file
# with open('now.csv', 'r') as f:
#     #reading the csv file
#     b = csv.reader(f)

#     #displaying all contents of the csv file
#     '''for lines in b:
#         print(lines) '''

    #find the value in the rows

#hoc tren youtube
csv_file = open('now.csv')

# next(csv_file) #skip the first title line (name, title, major,...)
# #print all rows
# for row in csv_file:
#     print(row)

#print all rows into list
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    #Name, Major, Year, CGPS = row
    #print(name, major, year, cgpa)
    if fields['Name'] == "Toan":
        msg = ACCEPTED_MSG.format(Name)

#close the csv file
csv_file.close()

