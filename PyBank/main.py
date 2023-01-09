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
    date = []

    for row in csvreader:
        month_count += 1
        total_prof_loss += int(row[1])
        change_prof_loss = int(row[1]) - prof_loss_last_month        
        prof_loss_last_month = int(row[1])
        list_change_prof_loss.append(change_prof_loss)
        date.append(row[0])

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
        
    maximum = max(list_change_prof_loss)
    minimum = min(list_change_prof_loss)
    
    for value in list_change_prof_loss:
        if value == maximum:
            imaximum = list_change_prof_loss.index(maximum)
        if value == minimum:
            iminimum = list_change_prof_loss.index(minimum)


    print("Financial Analysis")  
    print("----------------------------")  
    print("Total Months:", month_count)
    print(f"Total: ${total_prof_loss}")
    print(f"Average Change: ${round(average(list_change_prof_loss), 2)}")
    print(f"Greatest Increase in Profits: {date[imaximum + 1]} (${(maximum)})")
    print(f"Greatest Decrease in Profits: {date[iminimum + 1]} (${(minimum)})")
    
    # Set variable for and open the output file
    
    with open("analysis/budget_data_analysis_final.txt", "w") as file1:
        file1.write("Financial Analysis \n")
        file1.write(f"---------------------------- \n")
        file1.write(f"Total Months: {month_count} \n")
        file1.write(f"Total: ${total_prof_loss} \n")
        file1.write(f"Average Change: ${round(average(list_change_prof_loss), 2)} \n")
        file1.write(f"Greatest Increase in Profits: {date[imaximum + 1]} (${(maximum)}) \n")
        file1.write(f"Greatest Decrease in Profits: {date[iminimum + 1]} (${(minimum)}) \n")
    
    
    #References
    #MAX function in Python
    #https://www.geeksforgeeks.org/python-max-function/?ref=gcse
    #how to write in a file with Python (website in Portuguese (Brazil))
    #https://www.freecodecamp.org/portuguese/news/como-escrever-em-um-arquivo-em-python-open-read-append-e-outras-funcoes-de-manipulacao-explicadas/