import os
import csv

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
changes = []
dates = []

csvpath= os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    for row in csvreader:
        # Extract date and profit/loss
        date = row[0]
        profit_loss = int(row[1])
        
        # Count total months
        total_months += 1
        
        # Add to total profit/loss
        total_profit_losses += profit_loss
        
        # Calculate the monthly change if not the first row
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        # Update the previous profit/loss
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Find the greatest increase and decrease in profits
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0
greatest_increase_date = dates[changes.index(greatest_increase)] if changes else ""
greatest_decrease_date = dates[changes.index(greatest_decrease)] if changes else ""

# analysis summary
analysis_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis to the terminal
print(analysis_summary)

# Export the results to a text file
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write(analysis_summary)

