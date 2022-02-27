# The data we need to retrieve-
import os
import csv
#Imported dependencies

read_file=os.path.join('Resources','election_results.csv')
write_file=os.path.join('Analysis','election_analysis.txt')
#Assigning variable to file path with os.path.join('So that code works on different os')

with open(read_file, 'r') as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)

with open(write_file, 'w') as election_analysis:
    election_analysis.write('')
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote