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

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        
        # Increment the candidate's vote count
        candidates[candidate_name] += 1

# Determine winner
winner = max(candidates, key=candidates.get)

# Save results to text file
with open("election_results.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        vote_percentage = (votes / total_votes)*100
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")