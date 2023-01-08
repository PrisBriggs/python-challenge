# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv') 

with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read each row of data after the header
    csv_header = next(csvreader)
    
    # Setting initial value of the counter or total to zero
    month_count = 0
    total = 0   
    
    for row in csvreader:
        month_count += 1
        total += int(row[1])
    
    print("Financial Analysis")  
    print("----------------------------")  
    print("Total Months: ", month_count)
    print(f"Total: ${total}")
    
    
    
   

    

    