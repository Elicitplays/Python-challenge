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

def largest(arr, n):
 
    # Initialize maximum element
    max = arr[0]
 
    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
            max_position = i+2


    return max, max_position

def smallest(arr, n):
 
    # Initialize maximum element
    min = arr[0]
 
    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
            min_position = i+2
    return min, min_position



net_total = []
average_change = []
changes_month = []
first_pass = True
number_months = 0

with open(budgetDataPath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    
    
    for row in csv_reader:
        number_months = number_months + 1
        value_row = int(row[1])
        net_total.append(value_row)
        average_change.append(value_row)
    
    for i in range(1, len(average_change)):
        x = average_change[i] -average_change[i-1]
        changes_month.append(x)


    
    print("Financial Analysis")
    print("-------------------------------------")
    print(f"Total Months: {number_months}")
    print(f"Total: ${_sum(net_total)}" )
    main_divider = len(changes_month)
    length_array = len(changes_month)
    print(f"Average Change: ${round(((_sum(changes_month))/main_divider),2)}")
    a,b = largest(changes_month,length_array)
    c,d = smallest(changes_month,length_array)

with open((budgetDataPath)) as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)

    month_greatest = mycsv[b][0]
    month_decrease = mycsv[d][0]


    print(f"Greatest increase in Profits:{month_greatest} (${a})")
    print(f"Greatest decrease in Profits:{month_decrease} (${c})")

with open('analysis/Pybank_output.txt','w') as file:
    file.write("Financial analysis\n")
    file.write("-------------------------------------\n")
    file.write(f"Total Months: {number_months}\n")
    file.write(f"Total: ${_sum(net_total)}\n" )
    file.write(f"Average Change: ${round(((_sum(changes_month))/main_divider),2)}\n")
    file.write(f"Greatest increase in Profits:{month_greatest} (${a})\n")
    file.write(f"Greatest decrease in Profits:{month_decrease} (${c})\n")







