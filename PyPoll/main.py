import csv
import pandas as pd
import os 



csv_path = "election_data.csv"
file = pd.read_csv(csv_path)

# print(type(file))
# print(file.columns)
# print(file.head())



NumberOfVoters = file["Voter ID"].count()

# print(NumberOfVoters) # (int) The number of votes cast




Candidates = file.Candidate.unique()

# print(Candidates) # (array) the candidates who received votes




VoteCounts = file['Candidate'].value_counts()
Names = VoteCounts.keys().tolist()
Votes = VoteCounts.tolist()
NumberOfNames = len(Names)

# print(VoteCounts) # (Series) the candidates and the votes they recieved
# print(Names) # (array) the candidates sorted by popularity
# print(Votes) # (array) their votes recieved sorted by popularity
# print(NumberOfNames) # (int) number of candidates



Percents =[]
for x in range(0, NumberOfNames):
    Percents.append(round(Votes[x] / NumberOfVoters * 100, 3))

# print(Percents) # (array) the percent of votes recieved sorted by popularity



# print the results
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(NumberOfVoters))
print('-------------------------')
for x in range(0, NumberOfNames):
    print(str(Names[x]) + ': ' + str(Percents[x]) + '% (' + str(Votes[x]) + ')')
print('-------------------------')
print('Winner: ' + Names[0])
print('-------------------------')




# Create a .txt file with the results
with open('Election_Resuts.txt', 'w+', newline = "\n") as ER:
    ER.write('Election Results\n')
    ER.write('-------------------------\n')
    ER.write('Total Votes: ' + str(NumberOfVoters)+ "\n")
    ER.write('-------------------------\n')
    for x in range(0, NumberOfNames):
        ER.write(str(Names[x]) + ': ' + str(Percents[x]) + '% (' + str(Votes[x]) + ')\n')
    ER.write('-------------------------\n')
    ER.write('Winner: ' + Names[0] + '\n')
    ER.write('-------------------------\n')
    
# Enjoy!

