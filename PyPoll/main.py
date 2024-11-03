import csv
import os

# Connection string to .csv file
path = os.path.join("Resources", "election_data.csv")

# Variables tracked
total_votes = 0
candidates = {}
winner = None

# reading .csv file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
