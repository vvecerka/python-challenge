import os
import csv

# Initialize variables
total_votes = 0
candidate_votes = {}
candidate_list = []


csvpath= os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    
    for row in csvreader:
        # Extract candidate name from each row
        candidate = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the analysis summary
analysis_summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    analysis_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"
analysis_summary += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the analysis to the terminal
print(analysis_summary)

# Export the results to a text file
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as file:
    file.write(analysis_summary)