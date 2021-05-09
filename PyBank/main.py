
#Import modules
import csv

# Import csv and open textfile
data_file = "Resources/budget_data.csv"
export_file = open("analysis/financial_analysis.txt","w")

# Opening file
with open (data_file) as csvfile:
    header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    total_months = 0
    net_total = 0
    p_l_list = []
    pl_change_list = []
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        p_l_list.append(int(row[1]))
        #print(total_months, net_total, p_l_list)

    change = [pl_change_list.append(p_l_list[x+1] - p_l_list[x]) for x in range(len(p_l_list)) if (x+1) < len(p_l_list)]
    print(pl_change_list)

    sum = 0
    for x in pl_change_list:
        sum += x
    average_pl_change = sum/len(pl_change_list)

    print('Financial Analysis\n---------------------------------------------------------')
    print('Total Months: %d\n' % (total_months))
    print('Total: $%d\n' % (net_total))
    print('Average Change: $%0.2f\n' % (average_pl_change))
    print('Greatest Increase in Profits: %d\n' % (max(pl_change_list)))
    print('Greatest Decrease in Profits: %d\n' % (min(pl_change_list)))


export_file.write('Financial Analysis\n---------------------------------------------------------\n')
export_file.write('Total Months: %d\n' % (total_months))
export_file.write('Total: $%d\n' % (net_total))
export_file.write('Average Change: $%0.2f\n' % (average_pl_change))
export_file.write('Greatest Increase in Profits: %d\n' % (max(pl_change_list)))
export_file.write('Greatest Decrease in Profits: %d\n' % (min(pl_change_list)))


# Good practice to close files
export_file.close()