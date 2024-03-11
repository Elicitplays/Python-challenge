import os
import csv

ElectionDataPath = os.path.join("Resources","election_data.csv")

total_votes=0
charles_votes=0
diana_votes=0
raymon_votes=0

with open(ElectionDataPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] == "Charles Casper Stockham":
            charles_votes = charles_votes + 1
        elif row[2] == "Diana DeGette":
            diana_votes = diana_votes + 1
        else:
            raymon_votes = raymon_votes + 1
    
    charles_percentage = float((charles_votes/total_votes)*100)
    diana_percentage = float((diana_votes/total_votes)*100)
    raymon_percentage = float((raymon_votes/total_votes)*100)

    print("Election results")
    print("--------------------------")
    print(total_votes)
    
    
    print("--------------------------")
    print(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
    print(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
    print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})")
    print("--------------------------")
    
    if (charles_votes > diana_votes) & (charles_votes > raymon_votes):
        print("Winner: Charles Casper Stockham")
    elif (diana_votes > charles_votes) & (diana_votes > raymon_votes):
        print("Winner: Dianna DeGette")
    elif (raymon_votes > charles_votes) & (raymon_votes > diana_votes):
        print("Winner: Raymon Anthony Doane")

    print("--------------------------")

with open('Analysis/PyPoll_output.txt','w') as file:
    file.write("Election results\n") 
    file.write("--------------------------\n") 
    file.write(str(total_votes))
    file.write("\n")
    file.write("--------------------------\n")
    file.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n")
    file.write(f"Diana DeGette: {diana_percentage}% ({diana_votes})\n")
    file.write(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n")
    file.write("--------------------------\n")

    if (charles_votes > diana_votes) & (charles_votes > raymon_votes):
        file.write("Winner: Charles Casper Stockham\n")
    elif (diana_votes > charles_votes) & (diana_votes > raymon_votes):
        file.write("Winner: Dianna DeGette\n")
    elif (raymon_votes > charles_votes) & (raymon_votes > diana_votes):
        file.write("Winner: Raymon Anthony Doane\n")
    file.write("--------------------------\n")