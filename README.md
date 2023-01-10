# python-challenge

Georgia Tech Data Analytics BootCamp - January 2023

Homework Module 03 - Python Challenge
By Priscila Menezes Briggs

This challenge is divided into two separate analysis using different datasets.
The first challenge (PyBank) provides data about financial records from a company. The calculations that will be done in this challenge will quantify the changes in the company's profits within a designated period.
The second challenge (PyPoll) provides data about the election results from a small, rural town. The objectives of this challenge will be to identify the winner of the election and to count each candidate's votes, as well as the total amount of votes. 

PyBank 

In this challenge, a Python script has been developed to analyze the financial records of a company. 
A financial dataset called budget_data.csv had been provided, which is composed of two columns. 
The first column brings in each row the month and year of each measurement of profit/losses and is labeled with the title "Date". The period goes from January of 2010 to February of 2017. 
The second column is labeled with the title "Profit/Losses" and stores monthly values of profits (positive values) or losses (negative values) from the company.

The Python script analyzes the records to calculate each of the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

The script follows the steps below to calculate the results:

1) Import Modules
2) Set path for and open file with dataset
3) Skip the header row for the calculations
4) Set initial values of variables and lists to store data
5) Calculate the results
6) Print results to the terminal
7) Create text file to display the results

The file main.py inside the PyBank folder contains the Python script for this challenge and the file budget_data_analysis_final.txt reveals the results of the calculations performed by this script.

PyPoll

In this challenge, a Python script has been developed to analyze the election results of a small, rural town. 
A poll dataset called election_data.csv had been provided, which is composed of three columns. 
The first column is labeled with "Voter ID" and brings in each row the ID of each voter. There is no repetition of voters. 
The second column is labeled with the title "County" and shows the different counties were the votes were cast. 
The third column displays the name of the candidate for whom each voter voted. The column is labeled as "Candidate".

The Python script analyzes the records to calculate each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

The script follows the steps below to calculate the results:

1) Import Modules
2) Set path for and open file with dataset
3) Set initial values of variables and lists to store data 
4) Skip the header row for the calculations
5) Calculate the results
6) Print results to the terminal
7) Create text file to display the results

The file main.py inside the PyPoll folder contains the Python script for this challenge and the file poll_analysis_final.txt reveals the results of the calculations performed by this script.

The references to build these scripts were the activities and lessons given in class and the websites below. 

PyBank 
References
    websites visited in January/2023
    MAX function in Python
    #https://www.geeksforgeeks.org/python-max-function/?ref=gcse
    
    How to write in a file with Python (website in Portuguese (Brazil))
    #https://www.freecodecamp.org/portuguese/news/como-escrever-em-um-arquivo-em-python-open-read-append-e-outras-funcoes-de-manipulacao-explicadas/

PyPoll
 References
    websites visited in January/2023
    "Not in" statement in Python
    https://stackoverflow.com/questions/45707721/how-does-the-in-and-not-in-statement-work-in-python


All the files, scripts and information for this homework is found in the GitHub's repository on:

https://github.com/PrisBriggs/python-challenge
