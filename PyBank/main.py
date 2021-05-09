
#Import modules
import csv

# Import csv
data_file = "Resources/budget_data.csv"

# Opening file
with open (data_file) as csvfile:
    header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = 0
    net_total = 0
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        print(total_months, net_total)