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

month_to_number = {   "Jan": 1,
                   "Feb": 2,
                   "Mar":3,
                   "Apr":4,
                   "May":5,
                   "Jun":6,
                   "Jul":7,
                   "Aug":8,
                   "Sep":9,
                   "Oct":10,
                   "Nov":11,
                   "Dec":12}




#create csv with headers to store converted data
headers = ["Emp ID","First Name","Last Name", "DOB", "SSN", "State"]
newRow = {}
revenueChange = pd.DataFrame(columns=["Date","Revenue Change"])
#-----------------------------------------------------------
# Function Definitions
#-----------------------------------------------------------
#Function to format data output to both terminal and csv
def displayOutput(numMonths,totalRevenue,avgChange,maxChange,minChange):
    print()
    return

#convert month 3 letter abbreviation to number
def convertMonth(month):
    return(month_to_number[month])

#-----------------------------------------------------------
# Application Code
#-----------------------------------------------------------

#import budget csv files into DataFrame
budgetData = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
budgetData[["Month","Year"]] = budgetData["Date"].str.split('-',expand = True)

for index,row in budgetData.iterrows():
    row["Month"]= convertMonth(row["Month"])

#sort to get data in correct order
budgetData.sort_values(["Month","Year"])
print(budgetData)
#count number of months in dataset
numMonths = budgetData["Month"].count()

#calculate the total revenue over the time period listed in the dataset
totalRevenue = budgetData["Revenue"].sum()

#setup initial previousRevenue value to first value in budget data (will result in 0 change for first month)
previousRevenue = budgetData.iloc[0,1]
#Iterate over rows of budget data, creating a new dataframe that contains the change in revenue month to month
for index,row in budgetData.iterrows():
    change = row["Revenue"] - previousRevenue

    newRow = {"Date" : (str(row["Month"])+str(row["Year"])), "Revenue Change": change}
    revenueChange = revenueChange.append(newRow, ignore_index=True)
    previousRevenue = row["Revenue"]

print(revenueChange)



budgetData.to_csv(outputFilePath)