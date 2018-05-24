#Andrew Kling
#UNCC HW3
#PyBank - Reads in multiple .csv files containing monthly revenue data from a bank
#         Output will be pushed to new Revenue_Data_Summary.csv and terminal
#         Output contains:
#         -total count of months
#         -total revenue
#         -avg revenue change
#         -greatest increase in revenue (month-year and value)
#         -greatest decrease in revenue (month-year and value)

import os
import pandas as pd

#-----------------------------------------------------------
#Define Variables
#-----------------------------------------------------------

#setup input and output file paths
outputFilePath = os.path.join("PyBank","Revenue_Data_Summary.csv")
inputFilePath1 = os.path.join("PyBank","raw_data","budget_data_1.csv")
inputFilePath2 = os.path.join("PyBank","raw_data","budget_data_2.csv")
files = [inputFilePath1,inputFilePath2]

#create csv with headers to store converted data
headers = ["Emp ID","First Name","Last Name", "DOB", "SSN", "State"]

#-----------------------------------------------------------
# Function Definitions
#-----------------------------------------------------------

#Converts Name field to two seperate fields, first name and last name
def splitName(name):
    first, last = name.split(" ")
    print(f'First name: {first} | Last Name: {last}')
    return (first, last)



#-----------------------------------------------------------
# Application Code
#-----------------------------------------------------------

#create csv file and add headers
with open(outputFilePath,"w") as output:
    writer = csv.writer(output)
    writer.writerow(headers)

#iterate over all the files stored in array, converting columns
for f in files:
    with open(f, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            newRow=[]
            #if employee ID is not a number, probably header so skip
            if row[0].isdigit():
                newRow.insert(0,row[0])
                #split first and last name then insert last as new element
                first, last = splitName(row[1])
                newRow.insert(1, first)
                newRow.insert(2,last)
                #convert date to MM/DD/YYYY format
                newRow.insert(3,convertDate(row[2]))
                #Anonymize employee SSN
                newRow.insert(4, anonymizeSSN(row[3]))
                #convert state to abbreviation
                newRow.insert(5, stateAbbrev[row[4]])
                #append converted row to existing csv file
                with open(outputFilePath,"a") as output:
                    writer = csv.writer(output)
                    writer.writerow(newRow)
            


