import csv
import os

# Connection string to .csv file
path = os.path.join("Resources", "budget_data.csv")

# Variables tracked
month_count = 0
total_prof_loss = 0
changes = []
change_months = []
last_month = 0


# reading .csv file
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping first row and reading data
    header = next(csvreader)
    print(header)

    # Extracting first row
    first_row = next(csvreader)