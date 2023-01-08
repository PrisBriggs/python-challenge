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
    total_prof_loss = 0
    prof_loss_last_month = 0   
    list_change_prof_loss = []
    change_prof_loss = []

    for row in csvreader:
        month_count += 1
        total_prof_loss += int(row[1])
        change_prof_loss = int(row[1]) - prof_loss_last_month        
        prof_loss_last_month = int(row[1])
        list_change_prof_loss.append(change_prof_loss)

    #Removing the first item of the list to calculate the correct average 
    # (first item in list_change_prof_loss was the subtraction between the first element in row[1] and zero, which was the initial value of prof_loss_last_month.
    # However, only the subtraction of items inside the list should be considered to calculate the average)    
    list_change_prof_loss.pop(0)   
        
    def average(list):
        length = len(list)
        total_sum = 0
        for item in list:
            total_sum += item
        return total_sum / length
    
    
    print("Financial Analysis")  
    print("----------------------------")  
    print("Total Months: ", month_count)
    print(f"Total: ${total_prof_loss}")
    print(f"Average Change: ${round(average(list_change_prof_loss), 2)}")
    
    
    
   

    

    