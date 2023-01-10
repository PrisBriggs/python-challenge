# Importting Modules
import os
import csv

# Setting path for file
csvpath = os.path.join('.', 'Resources', 'election_data.csv') 

# Setting initial values of the counters to zero and setting up lists to store data
candidates_list = []
candidates_votes = []
candidates_percents = []
vote_count = 0
cand1_vcount = 0
cand2_vcount = 0
cand3_vcount = 0  

# Opening CSV file and storing it into an object
with open(csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Storing and skipping the header row in order to read each row of data after the header
    csv_header = next(csvreader)

    # Calculating the total number of votes  
    # Identifying names of each candidate and appending them to a designated list
    # Calculating amount of votes for each candidate
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
        
# Appending number of votes for each candidate to a designated list
candidates_votes.append(cand1_vcount)
candidates_votes.append(cand2_vcount)
candidates_votes.append(cand3_vcount)

# Calculating percentage of votes for each candidate
percent1 = round(int(cand1_vcount) / int(vote_count) * 100, 3)
percent2 = round(int(cand2_vcount) / int(vote_count) * 100, 3)
percent3 = round(int(cand3_vcount) / int(vote_count) * 100, 3)

# Appending percentage of votes for each candidate to a designated list   
candidates_percents.append(percent1)
candidates_percents.append(percent2)
candidates_percents.append(percent3)

# Identifying the value that represents the biggest amount of votes inside the correspondent list
winner = max(candidates_votes)

# Identifying the winner by comparing indexes of the biggest amount of votes with the candidates names' indexes
for vote in candidates_votes:
        if vote == winner:
            i_winner = candidates_votes.index(winner)


# Printing results to terminal
print("Election Results")  
print("-------------------------")  
print("Total Votes:", vote_count)
print("-------------------------")  
print(f"{candidates_list[0]}: {(percent1)}% ({(cand1_vcount)})")
print(f"{candidates_list[1]}: {(percent2)}% ({(cand2_vcount)})")
print(f"{candidates_list[2]}: {(percent3)}% ({(cand3_vcount)})")
print("-------------------------")  
print(f"Winner: {candidates_list[i_winner]}")
print("-------------------------")  


# Creating and opening the TXT file in the designated location and storing it into an object
# Writing results to TXT file    
with open("analysis/poll_analysis_final.txt", "w") as file2:
    file2.write("Election Results \n")
    file2.write(f"------------------------- \n")
    file2.write(f"Total Votes: {vote_count} \n")
    file2.write(f"------------------------- \n")
    file2.write(f"{candidates_list[0]}: {(percent1)}% ({(cand1_vcount)}) \n")
    file2.write(f"{candidates_list[1]}: {(percent2)}% ({(cand2_vcount)}) \n")
    file2.write(f"{candidates_list[2]}: {(percent3)}% ({(cand3_vcount)}) \n")
    file2.write(f"------------------------- \n")
    file2.write(f"Winner: {candidates_list[i_winner]} \n")
    file2.write("-------------------------")     