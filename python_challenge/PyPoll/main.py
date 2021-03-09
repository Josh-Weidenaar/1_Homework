# Import the OS Module to allow for use across systems
import os
import csv
non_vote_count = 0
vote_count = 0
cand0_count = 0
cand1_count = 0
cand2_count = 0
cand3_count = 0
counter = 0
elec_vot_list = []
elec_county_list = []
elec_cand_list = []
elec_unique_cand_list = []
vote_count_list = []
#Results_Dict = {'Candidate':[],'vote count':[]}
# define path * lines 5 - 22 pulled from python day 2 lesson 8*
csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Reads header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    
    # Read each row of data after the header
    for i in csvreader:
        
        #Read all values and append to lists
        Voter_ID = i[0]
        County = i[1]
        Candidate = i[2]
        elec_vot_list.append(Voter_ID)
        elec_county_list.append(County)
        elec_cand_list.append(Candidate)

        # Count total # of votes making sure the person actually voted for someone
        if not Candidate:
            non_vote_count = non_vote_count + 1
        else: 
            vote_count = vote_count + 1 


        # If candidate isn't in unique cand list, add the candidate to the unique list
        if Candidate not in elec_unique_cand_list:
            elec_unique_cand_list.append(Candidate)

    # Sum up total profits/losses
    for j in elec_cand_list:

        if elec_cand_list[counter] == elec_unique_cand_list[0]:
            cand0_count = cand0_count + 1
        elif elec_cand_list[counter] == elec_unique_cand_list[1]:
            cand1_count = cand1_count + 1 
        elif elec_cand_list[counter] == elec_unique_cand_list[2]:
            cand2_count = cand2_count + 1
        elif elec_cand_list[counter] == elec_unique_cand_list[3]:
            cand3_count = cand3_count + 1
        else: 
            print("oh no!")
        counter = counter + 1
    elec_vot_tup = tuple(elec_vot_list)
    elec_county_tup = tuple(elec_county_list)
    elec_cand_tup = tuple(elec_cand_list)
    Vote_in_tup = cand0_count + cand1_count + cand2_count + cand3_count
    
    # Add candidate vote counts to a list to find max then index that max value and identify the winner 
    vote_count_list.append(cand0_count)
    vote_count_list.append(cand1_count)
    vote_count_list.append(cand2_count)
    vote_count_list.append(cand3_count)
    vote_count_list_max = max(vote_count_list)
    index_vote_count_list_max = vote_count_list.index(vote_count_list_max)
    winner = elec_unique_cand_list[index_vote_count_list_max]


    print(f"Candidate {elec_unique_cand_list[0]} received {cand0_count} votes or {int((cand0_count/vote_count)*100)}% of votes.")

    print(f"Candidate {elec_unique_cand_list[1]} received {cand1_count} votes or {int((cand1_count/vote_count)*100)}% of votes.")

    print(f"Candidate {elec_unique_cand_list[2]} received {cand2_count} votes or {int((cand2_count/vote_count)*100)}% of votes.")

    print(f"Candidate {elec_unique_cand_list[3]} received {cand3_count} votes or {int((cand3_count/vote_count)*100)}% of votes.")

    print(f"The candidate {winner} won the election and is the newly elected Mayor, congratulations to Mayor {winner}!")

