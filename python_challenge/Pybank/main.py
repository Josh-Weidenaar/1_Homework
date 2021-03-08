# Import the OS Module to allow for use across systems
import os
import csv
# set counters at the beginning
counter = 0
tot = 0 
prolo_prev = 867884  
prolo_list = []

# define path * lines 5 - 22 pulled from python day 2 lesson 8*
csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    # Read each row of data after the header
    for i in csvreader:
        
        date = i[0]
        prof_los = i[1]
        # Change for the month appending to list
        prolo_change = prolo_prev - float(prof_los)
        prolo_list.append(float(prolo_change))
        prolo_prev = float(prof_los)

        # If date field isn't empty, count it as a month in the dataset
        if len(date) != 0:
            counter = counter + 1
        # Sum up total profits/losses
        tot = int(prof_los) + tot
    
    prolo_change = 0
    for i in prolo_list:
        prolo_change = prolo_change + i
        print(prolo_change)
    av_prolo = prolo_change/(counter - 1)
    print(f"Months in dataset: {counter}")
    print(f"Total profit/loss: ${tot}")
    print(f"Average profit/loss: ${av_prolo}")
