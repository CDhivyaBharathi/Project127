from os import access
import pandas as pd
import csv

df = pd.read_csv("ALL_STARS.csv")


del df["Star_Names"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df = df.rename({
   "Star_name_1" : "Star_name",
   "Distance_1" : "Distance",
   "Radius_1" : "Radius",
   "Mass_1" : "Mass"
} , axis="columns")

df.to_csv("Final.csv" , index = False)
