#Andrew Kling
#UNCC HW3
#PyBoss - Reads in employee information in a .csv and converts format
#         of data in columns

import os
import csv
import datetime

#-----------------------------------------------------------
#Define Variables
#-----------------------------------------------------------

#setup input and output file paths
outputFilePath = os.path.join("PyBoss","employee_data_converted.csv")
inputFilePath1 = os.path.join("PyBoss","raw_data","employee_data1.csv")
inputFilePath2 = os.path.join("PyBoss","raw_data","employee_data2.csv")
files = [inputFilePath1,inputFilePath2]
merged=[]

#create csv with headers to store converted data
headers = ["Emp ID","First Name","Last Name", "DOB", "SSN", "State"]

#Dictionary of state abbreviations
stateAbbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#-----------------------------------------------------------
# Function Definitions
#-----------------------------------------------------------

#Converts Name field to two seperate fields, first name and last name
def splitName(name):
    first, last = name.split(" ")
    print(f'First name: {first} | Last Name: {Last}')
    return first, last

#converts YYYY-MM-DD to MM/DD/YYYY 
def convertDate(date):
    date = date.split("-")
    newDate = date[1] + "/" + date[2] + "/" + date[0]
    return newDate

#converts first 5 digits of employee's SSN to *
def anonymizeSSN(ssn):
    ssn = snn.split("-")
    newSSN = "***-**-"+ssn[2]
    return newSSN

#-----------------------------------------------------------
# Application Code
#-----------------------------------------------------------


#iterate over all the files stored in array, converting columns
for f in files:
    with open(f, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
            for row in csvreader:
                newRow=[]
                #if employee ID is not a number, probably header so skip
                if row[0].isdigit():
                    newRow[0] = row[0]
                    #split first and last name then insert last as new element
                    first, last = splitName(row[1])
                    newRow[1] = first
                    newRow[2] = last
                    #convert date to MM/DD/YYYY format
                    newRow[3] = convertDate(row[2])
                    #Anonymize employee SSN
                    newRow[4] = anonymizeSSN(row[3])
                    #convert state to abbreviation
                    newRow[5] = stateAbbrev[row[4]]
                


