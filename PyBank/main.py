# Import Modules
import os
import csv

###Prompt user for title lookup
###book = input("What title are you looking for? ")

# Set path for file

csvpath = os.path.join('Resources', 'budget_data.csv') 

with open(csvpath, encoding='utf8') as csvfile:
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


   
   
    # Loop through looking for the video
    #for row in csvreader:
        #if row[0] == book:
           # print(row[0] + " was published by " + row[8] + " in " + row[9])

            # Set variable to confirm we have found the video
           # found = True


    # If the book is never found, alert the user
    #if found is False:
        #print("Sorry about this, we don't seem to have what you are looking for!")

       # with open(csvpath) as csvfile:

   


#References:
#https://www.geeksforgeeks.org/how-to-count-the-number-of-lines-in-a-csv-file-in-python/?ref=gcse