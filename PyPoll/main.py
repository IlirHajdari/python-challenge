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

    # Skipping first row and reading data
    header = next(csvreader)
    print(header)

    # Extracting data in each row
    for row in csvreader:
        print(". ", end="")

        # Increment total vote count
        total_votes += 1

        # Get candidates name from row
        candidate_name = row[2]
