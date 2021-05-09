
#Import modules
import csv

# Import csv and open textfile
data_file = "Resources/election_data.csv"
export_file = open("analysis/election_results.txt","w")

# Opening file
with open (data_file) as csvfile:
    header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    print("Works till here")

    total_votes = 0
    list_of_cadidates = ['Test1', 'Test2']
    for row in csvreader:

        #if len(list_of_cadidates) == 0:
        #    list_of_cadidates.append(row[2])

        total_votes += 1

        #for item in list_of_cadidates:
            #if item != row[2]:
                #list_of_cadidates.append(row[2])

    print(total_votes)
    print(list_of_cadidates)

export_file.write('Election Results\n---------------------------------------------------------\n')
export_file.write('Total Votes: %d\n' % (total_votes))

# Closing export file
export_file.close()