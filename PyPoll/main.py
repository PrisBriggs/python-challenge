# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join('.', 'Resources', 'election_data_test.csv') 

# Lists to store data
candidates_list = []
candidates_votes = []
candidates_percents = []
vote_count = 0
cand1_vcount = 0
cand2_vcount = 0
cand3_vcount = 0
poll_results = {}

with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read each row of data after the header
    csv_header = next(csvreader)
    
    for row in csvreader:
        vote_count += 1
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        if row[2] == candidates_list[0]:
            cand1_vcount += 1
        elif row[2] == candidates_list[1]:
            cand2_vcount += 1
        elif row[2] == candidates_list[2]:
            cand3_vcount += 1      
        

candidates_votes.append(cand1_vcount)
candidates_votes.append(cand2_vcount)
candidates_votes.append(cand3_vcount)

percent1 = round(int(cand1_vcount) / int(vote_count) * 100, 3)
percent2 = round(int(cand2_vcount) / int(vote_count) * 100, 3)
percent3 = round(int(cand3_vcount) / int(vote_count) * 100, 3)
   
candidates_percents.append(percent1)
candidates_percents.append(percent2)
candidates_percents.append(percent3)

winner = max(candidates_votes)

for vote in candidates_votes:
        if vote == winner:
            iwinner = candidates_votes.index(winner)


print("Election Results")  
print("-------------------------")  
print("Total Votes:", vote_count)
print("-------------------------")  
print(f"{candidates_list[0]}: {(percent1)}% ({(cand1_vcount)})")
print(f"{candidates_list[1]}: {(percent2)}% ({(cand2_vcount)})")
print(f"{candidates_list[2]}: {(percent3)}% ({(cand3_vcount)})")
print("-------------------------")  
print(f"Winner: {candidates_list[iwinner]}")
print("-------------------------")  

    #Set variable for and open the output file
    
with open("analysis/poll_analysis_final.txt", "w") as file2:
    file2.write("Election Results \n")
    file2.write(f"------------------------- \n")
    file2.write(f"Total Votes: {vote_count} \n")
    file2.write(f"------------------------- \n")
    file2.write(f"{candidates_list[0]}: {(percent1)}% ({(cand1_vcount)}) \n")
    file2.write(f"{candidates_list[1]}: {(percent2)}% ({(cand2_vcount)}) \n")
    file2.write(f"{candidates_list[2]}: {(percent3)}% ({(cand3_vcount)}) \n")
    file2.write(f"------------------------- \n")
    file2.write(f"Winner: {candidates_list[iwinner]} \n")
    file2.write("-------------------------")  
                 
        
    #References
    #MAX function in Python
    #https://www.geeksforgeeks.org/python-max-function/?ref=gcse
    #how to write in a file with Python (website in Portuguese (Brazil))
    #https://www.freecodecamp.org/portuguese/news/como-escrever-em-um-arquivo-em-python-open-read-append-e-outras-funcoes-de-manipulacao-explicadas/