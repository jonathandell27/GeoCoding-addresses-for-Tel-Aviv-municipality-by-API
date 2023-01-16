import os
import codecs
from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
import time
from datetime import datetime


print(time.ctime())
st = time.time()
#currentDirectory - Where the Python file is located
currentDirectory = os.getcwd()

df1 = pd.read_excel(r"{}\Tel Aviv addresses.xlsx".format(currentDirectory), sheet_name=0) #Full addresses sheet 
df2 = pd.read_excel(r"{}\Tel Aviv addresses.xlsx".format(currentDirectory), sheet_name=1) #Addresses sheet 
C1 = df1['Address'].tolist()
C2 = df1['Streets'].tolist()
C3 = df1['X'].tolist()
C4 = df1['Y'].tolist()
Streets = df2['Streets'].tolist()

for file in os.listdir(r"{}\Input".format(currentDirectory)):
    if file.endswith(".xlsx"):
        df3 = pd.read_excel(r"{}\Input\{}".format(currentDirectory,file), "Table") #sheet_name
        print(file)
        my_sheets = pd.ExcelFile(r"{}\Input\{}".format(currentDirectory,file))
        print(my_sheets.sheet_names)
        colunmslist = list(df3)
        print(colunmslist)
        T1 = df3[colunmslist[0]].tolist()
        my_sheets.close()


final_Streets = []
Streets_Ave = []

for T in T1:
    Avastreetfuzzy = []
    streetvalue = []
    for street in Streets:
        S1 = fuzz.partial_token_set_ratio(T,street)
        S2 = fuzz.partial_token_sort_ratio(T,street)
        S3 = fuzz.token_set_ratio(T,street)
        S4 = fuzz.token_sort_ratio(T,street)
        Avastreetfuzzy.append((S1+S2+S3+S4)/4)
        streetvalue.append(street)        
    Streets_Ave.append(max(Avastreetfuzzy))
    final_Streets.append(streetvalue[Avastreetfuzzy.index(max(Avastreetfuzzy))])    
 
def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1
    
final_numbers = []
Address_match = []
pointX = []
pointY = []    
    
for T in T1:
    Avafuzzy = []
    Address_value = []
    for street in final_Streets:       
        for C in C1[C2.index(street):rindex(C2,street)+ 1]:
            N1 = fuzz.partial_token_set_ratio(T,C)
            N2 = fuzz.partial_token_sort_ratio(T,C)
            N3 = fuzz.token_set_ratio(T,C)
            N4 = fuzz.token_sort_ratio(T,C)
            Avafuzzy.append((N1+N2+N3+N4)/4)
            Address_value.append(C)   


    final_numbers.append(max(Avafuzzy))
    Address_match.append(Address_value[Avafuzzy.index(max(Avafuzzy))])
    pointX.append(C3[C1.index(Address_match[-1])])
    pointY.append(C4[C1.index(Address_match[-1])])

    print("Complete {} from {}".format(len(final_numbers),len(T1)))


columns = ["Original table","Matching ratio","Match to address","X","Y"]


# Converting to excel
df = pd.DataFrame(list(zip(T1,final_numbers,Address_match,pointX,pointY)), columns = columns)

df.to_excel(r"{}\Output\Output.xlsx".format(currentDirectory))

et = time.time()
res = et - st
final_res = res / 60

print('Execution time:', final_res, 'minutes')

print(time.ctime())

print("Done!")












