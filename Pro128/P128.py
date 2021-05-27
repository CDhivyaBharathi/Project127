from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
print(page)

soup = bs(page.text,'html.parser')

table = soup.find_all('table')


temp_list= []
rows = table[4].find_all('tr')
for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)




Star_names_1 = []
DIstance_1 =[]
Mass_1 = []
Radius_1 =[]


for i in range(1,len(temp_list)):
    Star_names_1.append(temp_list[i][0])
    DIstance_1.append(temp_list[i][5])
    Mass_1.append(temp_list[i][7])
    Radius_1.append(temp_list[i][8])

df = pd.DataFrame(list(zip(Star_names_1,DIstance_1,Mass_1,Radius_1,)),columns=['Star_name_1','Distance_1','Mass_1','Radius_1'])
print(df)

df.to_csv('dwarf.csv' , index=False)