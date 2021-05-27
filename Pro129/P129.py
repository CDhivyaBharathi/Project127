import csv
import pandas as pd

data = pd.read_csv("dwarf.csv")

data["Radius_1"] = 0.102763 * data["Radius_1"]

print(data["Mass_1"])
data["Mass_1"] = data["Mass_1"]. dropna()
print(data["Mass_1"])

data["Mass_1"] = data.Mass_1.astype(float)
data["Mass_1"] = pd.to_numeric(data["Mass_1"], downcast='float')
data["Mass_1"] = 0.000954588*data["Mass_1"]

data.to_csv("dwarf_Final.csv" , index = False)

import csv

data1 = []
data2 = []

with open ("dwarf_Final.csv" , 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data1.append(row) 

with open ("stars.csv" , 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data2.append(row)

header_1 = data1[0]
header_2 = data2[0]

pl_data1 = data1[1:]
pl_data2 = data2[1:]

headers = header_1+header_2

pl_data =[]

for i in pl_data1:
    pl_data.append(i)
for j in pl_data2:
    pl_data.append(j)

with open("ALL_STARS.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)   
    csvwriter.writerows(pl_data)



