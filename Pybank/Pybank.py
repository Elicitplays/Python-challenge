import os
import csv

budgetDataPath = os.path.join("Resources","budget_data.csv")

def _sum(arr):
 
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0
 
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
 
    return(sum)



net_total = []

with open(budgetDataPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    
    for row in csv_header
        number_months = ++
        net_total.append(row[2])

