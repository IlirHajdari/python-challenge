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

    # Extracting data in each line
    for row in csvreader:
        # Counting number of months
        month_count += 1
        # Calculating total profit
        total_prof_loss = total_prof_loss + int(row[1])

        # Calculate and store profit/loss change
        if month_count > 1:
            change = current_month_profit_loss - last_month # type: ignore
            changes.append(change)
            change_months.append(row[0])

            # Calculate greatest profit increase and decrease
            greatest_increase = max(changes) if changes else 0
            greatest_increase_month = change_months[changes.index(greatest_increase)] if change else ""

            greatest_decrease = min(changes) if changes else 0
            greatest_decrease_month = change_months[changes.index(greatest_decrease)] if change else ""