#Andrew Kling
#UNCC HW3
#PyBank
# Reads in multiple .csv files containing monthly revenue data from a bank
# Output will be pushed to new Revenue_Data_Summary.csv and terminal
# Output contains:
# -total count of months
# -total revenue
# -avg revenue change
# -greatest increase in revenue (month-year and value)
# -greatest decrease in revenue (month-year and value)

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





#-----------------------------------------------------------
# Application Code
#-----------------------------------------------------------

##NOTES - use iloc with a for loop, using index to check values in current row and next row for month to
# month changes

#import budget data into DataFrame
budgetData = pd.concat((pd.read_csv(f) for f in files))

numMonths = budgetData["Date"].count()
print(numMonths)


