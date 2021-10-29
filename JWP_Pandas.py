#Joshua Pardridge
#IFT 360 Assignment 2 - Part 1 (Pandas)

#Import pandas
from numpy import NaN
import pandas as pd

#Define variable xlsx_path and point it to the dataframe excel file
xlsx_path='pandas.xlsx'

#(1)Define dataframes (1 created in excel and one local)
exceldf=pd.read_excel(xlsx_path)

localdata = [["Anastasia", 12.5, 1, "yes"], ["Dima", 9, 3, "no"], ["Katherine", 16.5, 2, "yes"], ["James", NaN, 3, "no"], ["Emily", 9, 2, "no"]]
localdf = pd.DataFrame(localdata, columns= ["Name", "Score", "Attempts", "Qualify"])

#(2)Extract Emily's details from the Dataframe (local)
emilydetail = localdf.loc[[4]]
print (emilydetail)

#(3)Find the names of all persons registered
registered = localdf[['Name']]
print (registered)

#(4)Find the average # of attempts
attemptsaverage = localdf[['Attempts']].mean()
print (attemptsaverage)

#(5)Try reading data stored in an excel file (will read Dima row)
readingfile = exceldf.loc[[1]]
print (readingfile)

#(6)Print the number of rows and columns in the dataframe
rowsandcolumns = exceldf.shape
print (rowsandcolumns)

#(7)Extract subset from dataframe (First 2 rows)
subsetdf = exceldf.iloc[0:2]
print (subsetdf)

#(8)Save subset as a new csv file
subsetdf.to_csv('subsetdf.csv')

