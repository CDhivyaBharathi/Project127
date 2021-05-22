import pandas as pd 
import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = requests.get(START_URL)
print(browser)

soup = BeautifulSoup(browser.text , "html.parser")

table = soup.find('table')

temp_list = []

rows = table.find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

headers = ['Star_Names' , 'Distance' , 'Mass' , 'Radius']
str_data = []

for i in range(1 , len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

str_data.append(name)
others = [distance,mass,radius]
str_data.extend([others])
print("name",str_data)

df = pd.DataFrame(list(zip(name,distance,mass,radius)) , columns = ['Star_Names' , 'Distance' , 'Mass' , 'Radius'])
print(df)

df.to_csv('Stars.csv', index=False)