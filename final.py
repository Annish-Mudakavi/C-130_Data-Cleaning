import csv

#Creating two empty dataframe. 
datasets_1 = []
datasets_2 = []
with open("hello.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        datasets_1.append(row)

# Sorting planet names in alphabetical order
with open("datasets_2_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        datasets_1.append(row)

headers_1 = datasets_1[0]
headers_2 = datasets_2[0]

planets_data_1 = datasets_1[1:]
planets_data_2 = datasets_2[1:]

headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planets_data_1):
    planet_data.append(planets_data_1[index] + planets_data_2[index])

with open("final_2.csv", "a+") as f:
    csvwriter =  csv.writers(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data) 

