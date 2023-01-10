# Importting Modules
import os
import csv

# Setting path for file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv') 

# Opening CSV file and storing it into an object
with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Storing and skipping the header row in order to read each row of data after the header
    csv_header = next(csvreader)
    
    # Setting initial values of the counter and summations to zero and setting up lists to store data
    month_count = 0
    total_prof_loss = 0
    prof_loss_last_month = 0   
    list_change_prof_loss = []
    change_prof_loss = []
    date = []

    # Calculating the amount of months and total profits/losses
    # Calculating the changes in profit/losses over the entire period by subtracting the current month's value from the next month's value and then... 
    # ...appending results to correspondent list
    # Appending dates to corresponding list
    for row in csvreader:
        month_count += 1
        total_prof_loss += int(row[1])
        change_prof_loss = int(row[1]) - prof_loss_last_month        
        prof_loss_last_month = int(row[1])
        list_change_prof_loss.append(change_prof_loss)
        date.append(row[0])

    # Removing the first item of the list to calculate the correct average 
    # (first item in list_change_prof_loss was the subtraction between the first element in row[1] and zero, which was the initial value of prof_loss_last_month....
    # ...However, only the subtraction of items inside the list should be considered to calculate the average)    
    list_change_prof_loss.pop(0)   
    
    # Starting the calculation of the average change in profit/losses by defining the average function
    def average(list):
        length = len(list)
        total_sum = 0
        for item in list:
            total_sum += item
        return total_sum / length

    # Calculating maximum and minimum values for profit/losses    
    maximum = max(list_change_prof_loss)
    minimum = min(list_change_prof_loss)
    
    # Identifying the indexes of the maximum and minimum values for profit/losses inside the list_change_prof_loss list
    for value in list_change_prof_loss:
        if value == maximum:
            i_maximum = list_change_prof_loss.index(maximum)
        if value == minimum:
            i_minimum = list_change_prof_loss.index(minimum)


    # Printing results to terminal
    print("Financial Analysis")  
    print("----------------------------")  
    print("Total Months:", month_count)
    print(f"Total: ${total_prof_loss}")
    print(f"Average Change: ${round(average(list_change_prof_loss), 2)}")
    print(f"Greatest Increase in Profits: {date[i_maximum + 1]} (${(maximum)})")
    print(f"Greatest Decrease in Profits: {date[i_minimum + 1]} (${(minimum)})")
    

    # Creating and opening the TXT file in the designated location and storing it into an object
    # Writing results to TXT file
    with open("analysis/budget_data_analysis_final.txt", "w") as file1:
        file1.write("Financial Analysis \n")
        file1.write(f"---------------------------- \n")
        file1.write(f"Total Months: {month_count} \n")
        file1.write(f"Total: ${total_prof_loss} \n")
        file1.write(f"Average Change: ${round(average(list_change_prof_loss), 2)} \n")
        file1.write(f"Greatest Increase in Profits: {date[i_maximum + 1]} (${(maximum)}) \n")
        file1.write(f"Greatest Decrease in Profits: {date[i_minimum + 1]} (${(minimum)}) \n")    