#Andrew Kling
#UNCC HW3
#PyPoll
#Read in csv files (2 but can scale to more) that contains 3 headers:
#Voter Id, County and Candidate Selection.  main.py will read in these 
#.csv files and output to both the terminal and a text file the following:
#-Total votes cast
#-complete list of candidates who recieved votes
#-percentage of votes each candidate won
#-total number of votes each candidate won
#-winner of the election based on popular vote

import os
import pandas as pd

#-----------------------------------------------------------
#Define Variables
#-----------------------------------------------------------

#setup input and output file paths
outputFilePath = os.path.join("PyPoll","Election_Results.txt")
inputFilePath1 = os.path.join("PyPoll","raw_data","election_data_1.csv")
inputFilePath2 = os.path.join("PyPoll","raw_data","election_data_2.csv")
files = [inputFilePath1,inputFilePath2]

#format floats to display as percentage
pd.options.display.float_format = '{:.2f}%'.format

#-----------------------------------------------------------
# Function Definitions
#-----------------------------------------------------------
def printResults(totalVotes, candidateVotes, winner):
    #format results for printing to console and text file
    print("Election Results")
    print("---------------------------------------")
    print(f"Total Votes: {totalVotes}")
    print("---------------------------------------")
    for index, row in candidateVotes.iterrows():
        print(f'{row["Candidate"]}: {"{0:.1%}".format(row["Percent of Total Vote"])} ({row["Total Votes"]})')
    print("---------------------------------------")
    print(f"Winner: {winner}")
    print("---------------------------------------")

    #write to text file
    file = open(outputFilePath,"w")

    file.writelines("Election Results\n")
    file.write("---------------------------------------\n")
    file.write(f"Total Votes: {totalVotes} \n")
    file.write("---------------------------------------\n")
    for index, row in candidateVotes.iterrows():
        file.write(f'{row["Candidate"]}: {"{0:.1%}".format(row["Percent of Total Vote"])} ({row["Total Votes"]})\n')
    file.write("---------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("---------------------------------------\n")
    file.close()
    return

#-----------------------------------------------------------
# Application Code
#-----------------------------------------------------------
#import election data into DataFrame
electionData = pd.concat((pd.read_csv(f) for f in files))

#count all votes to get number of total votes
totalVotes = electionData["Candidate"].count()

#create dataframe containing candidate names and home many votes each got
candidateVotes = pd.DataFrame(electionData["Candidate"].value_counts().reset_index())
candidateVotes = candidateVotes.rename(index=str, columns={"index":"Candidate","Candidate":"Total Votes"})

#add column to dataframe with percent of total votes each candidate recieved
candidateVotes["Percent of Total Vote"] = (candidateVotes["Total Votes"] / totalVotes)

#Determine winner, who will be in first row of dataframe since it is sorted by value_counts()
winner = candidateVotes.iloc[0,0]

#Print results to console and text file
printResults(totalVotes, candidateVotes, winner)