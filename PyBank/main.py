# import your libraries
import csv
import pandas as pd
import os 




# find the file and call it 'file'
csv_path = "budget_data.csv"
file = pd.read_csv(csv_path)

# An alternate method:
# csvpath = os.path.join('budget_data.csv')
# with open(csvpath, 'r', newline='') as csvfile:
#     file = csv.reader(csvfile, delimiter=',')



# fix the mislabled column 
file = file.rename(columns={"Revenue":"Profit/Loss"})



# Create a variable equal to the number of months in the file
Months = file['Date'].count()



# The total net amount of "Profit/Losses" over the entire period
Sum = file['Profit/Loss'].sum()



Profits = file['Profit/Loss'] # create a column/array to hold the new 'change in profits' data 
PrevProf = Profits[0] # the profits of the previous month 
ChangesInProfits = [] # the new Array 

# add the change to the new array
# and update the previous month's profit 
for row in Profits: 
    ChangesInProfits.append(row - PrevProf) 
    PrevProf = row 



# add this new "Change in Profit/Loss" column to the file
file["Change in Profit/Loss"] = ChangesInProfits



# The average change in "Profit/Losses" between months over the entire period

# this one finds it using the array
AverageChange = sum(ChangesInProfits) / len(ChangesInProfits)

# This one finds it using the dataframe
AverageChange2 = file['Change in Profit/Loss'].mean()



# The greatest increase and decrease in profits over the entire period
MaxIncrease = file['Change in Profit/Loss'].max()
MinIncrease = file['Change in Profit/Loss'].min()
# index the dataframe by the change to loc(ate) the date 
IndexedFile = file.set_index('Change in Profit/Loss')
MaxDate = IndexedFile.loc[MaxIncrease, "Date"]
MinDate = IndexedFile.loc[MinIncrease, "Date"]



# Return the results 
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(Months))
print('Total: $' + str(round(Sum, 2)))
print('Average Change: $' + str(round(AverageChange2, 2)))
print('Greatest Increase in Profits: ' + str(MaxDate) + ' ($' + str(MaxIncrease) + ')')
print('Greatest Decrease in Profits: ' + str(MinDate) + ' ($' + str(MinIncrease) + ')')



# Create a text file with the results
with open('Bank_Results.txt', 'w+', newline = "\n") as w:
    w.write("Financial Analysis\n")
    w.write('----------------------------\n')
    w.write('Total Months: 41\n')
    w.write('Total: $18971412\n')
    w.write('Average Change: $-6594.12\n')
    w.write('Greatest Increase in Profits: Feb-16 ($1837235)\n')
    w.write('Greatest Decrease in Profits: Aug-14 ($-1779747)\n')



