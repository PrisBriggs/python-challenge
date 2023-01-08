# Import Modules
import os
import csv

###Prompt user for title lookup
###book = input("What title are you looking for? ")

# Set path for file

csvpath = os.path.join('.', 'Resources', 'budget_data.csv') 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Setting initial value of the counter to zero
    month_count = 0
       
    # Skip the header row
    csv_header = next(csvreader)
  
    # Read each row of data after the header
    for row in csvreader:
        month_count += 1

    print("Financial Analysis")  
    print("----------------------------")  
    print("Total Months: ", month_count)

y1=52
x = 0
def net_profit_losses(csvreader):
    row = int(csvreader[1])
    for row in csvreader:
        x += row
    return x
print(x)