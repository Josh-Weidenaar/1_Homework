# Import the OS Module to allow for use across systems
import os
import csv
# set counters at the beginning
counter = 0
tot = 0 
prolo_prev = 867884  
prolo_list = []
prolo_year_list = []
prolo_prolo_list = []

# define path * lines 5 - 22 pulled from python day 2 lesson 8*
csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Reads header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    
    # Read each row of data after the header
    for i in csvreader:
        
        date = i[0]
        prof_los = i[1]
        prolo_year_list.append(date)
        prolo_prolo_list.append(i[1])
        # Change for the month appending to list
        prolo_change = prolo_prev - float(prof_los)
        prolo_list.append(float(prolo_change))
        prolo_prev = float(prof_los)

        # If date field isn't empty, count it as a month in the dataset
        if len(date) != 0:
            counter = counter + 1
        # Sum up total profits/losses
        tot = int(prof_los) + tot
    #iterate through list made to add change together then divide by # of months - 1 for one fewer instance of change
    prolo_change = 0
    #finding biggest change in profits/losses to then print out corresponding values in other lists (negative for increase and positive for decrease)
    index_change_loss = prolo_list.index(max(prolo_list))
    index_change_Gain = prolo_list.index(min(prolo_list))

    #iterate through prololist to get avg change
    for i in prolo_list:
        prolo_change = prolo_change + i
    av_prolo = prolo_change/(counter - 1)

    #print all my found values
    print("FINANCIAL ANALYSIS")
    print("-------------------------------------------------------------------------------------------------")
    print(f"Months in dataset: {counter}")
    print(f"Total profit/loss: ${tot}")
    print(f"Average monthly change in profit/loss: ${av_prolo}")
    print(f"In {prolo_year_list[index_change_Gain]} the firm made ${abs(prolo_list[index_change_Gain])} dollars, the greatest increase in profits in this series.")
    print(f"In {prolo_year_list[index_change_loss]} the firm lost ${prolo_list[index_change_loss]} dollars, the greatest decrease in profits in this series.")
    
    # next step is to write to csv for pybank and then develop pypoll analysis