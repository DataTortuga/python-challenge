
#Import modules
import csv

# Import csv and open textfile
data_file = "Resources/election_data.csv"
export_file = open("analysis/financial_analysis.txt","w")

# Opening file
with open (data_file) as csvfile:
    header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')

    