import csv
import pandas as pd

data = pd.read_csv("dwarf.csv")

data["Radius"] = 0.102763 * data["Radius"]

print(data["Mass"])
data["Mass"] = data["Mass"]. dropna()
print(data["Mass"])

data["Mass"] = data.Mass.astype(float)
data["Mass"] = pd.to_numeric(data["Mass"], downcast='float')
data["Mass"] = 0.000954588*data["Mass"]

data.to_csv("dwarf_Final.csv")

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



