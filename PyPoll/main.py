# import modules
import csv
import os

# store file path using os
pypoll_csv_path = os.path.join("Resources", "election_data.csv")

# initalize/declare lists here
voter_id= []
countries=[]
candidates=[]
candidate_name= []
winner= []
khan = []
correy = []
li = []
otooley = []

# open file in read mode
with open(pypoll_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
# label header row as csv_reader, also skipping first line
    csv_header = next(csv_reader)

#  append votes, countries, and candidates columns (initalized above)
    for row in csv_reader:
        voter_id.append(row[0])
        countries.append(row[1])
        candidates.append(str(row[2]))
#  The total number of votes cast
    total_votes_cast= (len(voter_id))
# The total number of votes each candidate won
    for row[2] in candidates:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            # votes_received[0] += 1
            khan.append(candidates)
            khan_votes = len(khan)
        elif row[2] == candidate_name[1]:
            # votes_received[1] += 1
            correy.append(candidates)
            correy_votes = len(correy)
        elif row[2] == candidate_name[2]:
            # votes_received[2] += 1
            li.append(candidates)
            li_votes = len(li)
        elif row[2] == candidate_name[3]:
            # votes_received[3] += 1
            otooley.append(candidates)
            otooley_votes = len(otooley)
# The percentage of votes each candidate won
    khan_percent = round(((khan_votes / total_votes_cast) * 100), 2)
    correy_percent = round(((correy_votes / total_votes_cast) * 100), 2)
    li_percent = round(((li_votes / total_votes_cast) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes_cast) * 100), 2)
    
# The winner of the election based on popular vote.
    if khan_votes > max(correy_votes, li_votes, otooley_votes):
        winner = "Khan"
    elif correy_votes > max(khan_votes, li_votes, otooley_votes):
        winner = "Correy"  
    elif li_votes > max(correy_votes, khan_votes, otooley_votes):
        winner = "Li"
    else:
        winner = "O'Tooley"

# print in terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes_cast}")
print(f"-------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# export a text file with the results
output_path = os.path.join("Analysis", "Election Analysis.txt")
with open(output_path, 'w', newline='') as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {total_votes_cast}", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Khan: {khan_percent}% ({khan_votes})", file=text_file)
    print(f"Correy: {correy_percent}% ({correy_votes})", file=text_file)
    print(f"Li: {li_percent}% ({li_votes})", file=text_file)
    print(f"O'Tooley: {otooley_percent}% ({otooley_votes})", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print(f"-------------------------", file=text_file)