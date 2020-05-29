# import modules
import csv
import os

# store file path using os
pybank_csv_path = os.path.join("Resources", "budget_data.csv")

# initalize/declare lists here
# REMEBER: cant use append on int
total_months= []
net_profit_loss= []
avg_change_profit_loss= []

# open file in read mode
with open(pybank_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
# label header row as csv_reader, also skipping first line
    csv_header = next(csv_reader)  

# total number of months included in dataset, total profit in dataset
    for row in csv_reader:
        total_months.append(row[0])
        net_profit_loss.append(row[1])
# net total amount of "Profit/Losses" over entire period
    # remeber to take lines out of loops when done to prevent uneccessary looping
    # try "map" feature from week 4 pandas
    net_profit_loss_int = map(int, net_profit_loss)
    total_revenue = (sum(net_profit_loss_int))
# The average of the changes in "Profit/Losses" over the entire period
# cant use "net_profit_loss_int" bc int type has no length, len refers to len of a list, so define the list as int each time
    for i in range(len(net_profit_loss) - 1):
        profit_loss_change = int(net_profit_loss[i+1]) - int(net_profit_loss[i])
        avg_change_profit_loss.append(profit_loss_change)
# calculate monthly change in profit/loss  
    total_amount = sum(avg_change_profit_loss)
    avg_monthly_change = total_amount/ len(avg_change_profit_loss)
    avg_monthly_change = round(avg_monthly_change, 2)
# use avg_monthly_change to find the greatest increase in profits (date and amount) over the entire period
    profit_loss_inc = max(avg_change_profit_loss)
    k = avg_change_profit_loss.index(profit_loss_inc)
    total_month_inc = total_months[k+1]
# Use avg_monthly_change to find the greatest decrease in losses (date and amount) over the entire period
    profit_loss_dec = min(avg_change_profit_loss)
    j = avg_change_profit_loss.index(profit_loss_dec)
    total_month_dec = total_months[j+1]
# Print in terminal
print(f'Financial Analysis')
print(f'----------------------------')
print(f"Total Months:  {str(len(total_months))}")
print(f"Total: ${str(total_revenue)}")  
print(f"Average Change: $ {str(avg_monthly_change)}")
print(f"Greatest Increase in Profits: {total_month_inc} (${profit_loss_inc})")
print(f"Greatest Decrease in Profits: {total_month_dec} (${profit_loss_dec})")
# export a text file with the results
output_path = os.path.join("Analysis", "Financial Analysis.txt")
with open(output_path, 'w', newline='') as text_file:
    print("Financial Analysis", file=text_file)
    print('----------------------------', file=text_file)
    print(f"Total Months: {str(len(total_months))}", file=text_file)
    print(f"Total: ${str(total_revenue)}", file=text_file)
    print(f"Average Change: ${str(avg_monthly_change)}", file=text_file)
    print(f"Greatest Increase in Profits: {total_month_inc} ({profit_loss_inc})", file=text_file)
    print(f"Greatest Decrease in Profits: {total_month_dec} ({profit_loss_dec})",file=text_file)