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
        current_month_profit_loss = int(row[1])
        total_prof_loss += current_month_profit_loss

        # Calculate and store profit/loss change
        if month_count > 1:
            change = current_month_profit_loss - last_month # type: ignore
            changes.append(change)
            change_months.append(row[0])
        
        # Update last month's profit/loss to current month
        last_month = current_month_profit_loss

# Calculates average change
if changes:
    average_change = sum(changes) / len(changes)
    greatest_increase = max(changes)
    greatest_increase_month = change_months[changes.index(greatest_increase)]
    greatest_decrease = min(changes)
    greatest_decrease_month = change_months[changes.index(greatest_decrease)]
else:
    average_change = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

# Printing results to the Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months {month_count}")
print(f"Total: ${total_prof_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# Printing results to text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {month_count}\n")
    txt_file.write(f"Total: ${total_prof_loss}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")