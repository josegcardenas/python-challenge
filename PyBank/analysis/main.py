import os
import csv
PyBankcsv = os.path.join('..', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#variables
date = []
money = []
sum_total = 0
total_months = len(date)
increase = 0
decrease = 0
    
with open(PyBankcsv, newline='') as csvfile:   
    csvreader = csv.reader(csv_file, delimiter= ',')
    next(csvreader, None)
    print(f"Header: {csv_header}")
   #run loop to increase counters
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        sum_total += float(row[1])
#loop through to find increase and decrease
    for i in range (len(money)):
        if money [i] >= increase:
            increase = money[i]
            increase_month = date[i]
        elif money[i] <= decrease:
            decrease = money[i]
            decrease_month = date[i]
    else:
        print("No change")

#Average Profit/Loss
avg_money = round(sum_total/total_months, 2)
    

#output
with open ('output_financial.txt', "w", newline = '') as textfile:
    print("Financial Analysis", file = textfile)
    print("-------------------------------------")
    print(f'Total Months: {months}', file = textfile)
    print(f'Total Revenue: ${sum_total}', file = textfile)
    print(f'Average Profit/Loss Change: ${avg_money}', file = textfile)
    print(f'Greatest Increase/Loss: {increase_month}(${increase}', file = textfile)
    print(f'Greatest Decrease/Loss: {decrease_month}(${decrease})', file = textfile)
    print("-------------------------------------")

with open('output_financial.txt', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        print(row)    

