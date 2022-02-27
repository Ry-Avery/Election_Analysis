import os
import csv
# Imported dependencies

read_file=os.path.join('Resources','election_results.csv')
write_file=os.path.join('Analysis','election_analysis.txt')
# Assigning variable to file path with os.path.join('So that code works on different os')
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=''
winning_count=0
winning_percentage=0

with open(read_file, 'r') as election_data:
    file_reader=csv.reader(election_data)
    # Assigned variable to read data from election_results.csv
    for row in file_reader:
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        # If candidate name hasn't appeared before then add name to lists and dictionaries
        candidate_votes[candidate_name]+=1
        total_votes+=1
    # Cycled through rows in election_results.csv

for candidate_name in candidate_options:
    votes=candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100
    print(f'{candidate_name}- {votes:,} votes, {vote_percentage:.1f}% of the total vote.')
    if votes>winning_count:
        winning_candidate=candidate_name
        winning_count=votes
        winning_percentage=vote_percentage
    # If candidate has the most votes so far, assign them the winner
# Looped through each candidates stats

print(
    f'\n'
    f'{winning_candidate} won the election with {winning_count:,} votes of {total_votes:,} total votes({winning_percentage:.2f}%).'
    f'\n')

# with open(write_file, 'w') as election_analysis:
#     election_analysis.write('')