import csv

#creating empty dataframe called data
data = []
with open("dataset_2.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
header = data[0]
planet_data = data[1:]

# Converting all planet names to lower case
for datapoint in planet_data:
    datapoint[2] = datapoint[2].lower()

# Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[2])
with open("datasets_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)
