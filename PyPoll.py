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
# Opens and reads from election_results.csv and then closes file
    file_reader=csv.reader(election_data)
    # Assigned variable to read data from election_results.csv
    headers=next(file_reader)
    #Skipped header row
    for row in file_reader:
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        # If candidate name hasn't appeared before then add name to lists and dictionaries
        candidate_votes[candidate_name]+=1
        total_votes+=1
    # Cycled through rows in election_results.csv

with open(write_file, 'w') as election_analysis:
# Opens and writes from election_analysis.txt and then closes file
    election_heading=(
        f'\nElection Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_heading,end='')
    election_analysis.write(election_heading)
    # Prints and writes election heading
    for candidate_name in candidate_options:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(f'{candidate_name}- {votes:,} votes, {vote_percentage:.1f}% of the total vote.\n')
        print(candidate_results)
        election_analysis.write(candidate_results)
        # Prints and writes candidate results
        if votes>winning_count:
            winning_candidate=candidate_name
            winning_count=votes
            winning_percentage=vote_percentage
        # If candidate has the most votes so far, assign them the winner
    # Looped through each candidates stats
    canididate_winner=(
         f'-------------------------\n'
         f'{winning_candidate} won the election with {winning_count:,} votes of {total_votes:,} total votes({winning_percentage:.2f}%).\n'
         f'-------------------------\n')
    print(canididate_winner)
    election_analysis.write(canididate_winner)
    # Prints and writes election winner