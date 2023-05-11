import os
from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
import time
from datetime import datetime
import arcpy
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

print(time.ctime())
st = time.time()
#currentDirectory - Where the Python file is located
currentDirectory = os.getcwd()

username = os.getlogin()

print("Hello {}!".format(username))

#Connects to the Addresses layer in IView2
print("Connects to the Addresses layer in IView2")
table = "https://dgt-ags02/arcgis/rest/services/IView2/MapServer/527"
tableFields = [i.name for i in arcpy.ListFields(table)]
dftable = pd.DataFrame.from_records(data=arcpy.da.SearchCursor(table,tableFields),columns=tableFields)
dftable = dftable.sort_values(by='t_rechov')

C1 = dftable['t_ktovet_melea'].tolist()
C2 = dftable['t_rechov'].tolist()
C3 = dftable['x'].tolist()
C4 = dftable['y'].tolist()
C5 = dftable['k_rechov'].tolist()
Streets = list(set(C2))
Streets = sorted(Streets)

root = Tk()

Inputlist = []

Eraselist = []

savenamelist = []

print("ready for the user interface")

def Inputfun():
    root.directory = filedialog.askopenfilename()
    InputLayer = root.directory
    Input= r'{}'.format(InputLayer) #Select from a folder
    if len(Inputlist) < 1 :
        Inputlist.append(Input)
    else:
        Inputlist.remove(Inputlist[0])
        Inputlist.append(Input)
    path1.config(text="{}".format(Inputlist[0]))
    
def savefile():
    savepath = filedialog.askdirectory()
    savename = savepath
    if len(savenamelist) < 1 :
        savenamelist.append(savename)
    else:
        Eraselist.remove(savenamelist[0])
        Eraselist.append(savename)
    path3.config(text="{}".format(savenamelist[0]))
    
def run ():
    print('we started! If you see a "not responding" message - ignore it, it will pass after about 20 seconds')
    df1 = pd.read_excel(r"{}".format(Inputlist[0]),sheet_name="{}".format(text1.get()))
    T1 = df1["{}".format(text.get())].tolist()

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
    
    final_numbers = []
    Address_match = []
    pointX = []
    pointY = []   
    k_rechov = [] 
    
    print("nice.let's run!")

    def rindex(mylist, myvalue):
        return len(mylist) - mylist[::-1].index(myvalue) - 1  

    for T in T1:
        Avafuzzy = []
        Address_value = []
        street = final_Streets[T1.index(T)]   
        for C in C1[C2.index(street):rindex(C2,street)+ 1]:
            N1 = fuzz.partial_token_set_ratio(T,C)
            N2 = fuzz.partial_token_sort_ratio(T,C)
            N3 = fuzz.token_set_ratio(T,C)
            N4 = fuzz.token_sort_ratio(T,C)
            score = (N1+N2+N3+N4)/4
            Avafuzzy.append(score)
            Address_value.append(C)
            if score == 100:
                break
                                   
        final_numbers.append(max(Avafuzzy))
        Address_match.append(Address_value[Avafuzzy.index(max(Avafuzzy))])
        pointX.append(C3[C1.index(Address_match[-1])])
        pointY.append(C4[C1.index(Address_match[-1])])
        k_rechov.append(C5[C1.index(Address_match[-1])])

        print("Complete {} from {}".format(len(final_numbers),len(T1)))


    columns = ["Original table","Match to address","k_rechov","X","Y","Matching ratio"]


    # Converting to excel
    df2 = pd.DataFrame(list(zip(T1,Address_match,k_rechov,pointX,pointY,final_numbers)), columns = columns)
    
    df = pd.concat([df1, df2], axis=1)

    df.to_excel(r"{}\Output.xlsx".format(savenamelist[0]))
    
    endtxt.config(text="The process was completed successfully!")
    
    print("The process was completed successfully!")
    print("Good work {}".format(username))
    print("\N{smiling face with sunglasses}")
    print("You can turn off the tool and be impressed from the results")


root.title("GeoCode TLV")
root.geometry('600x600')
button1 = Button(root, text="Input Excel Table",bg='#0052cc', fg='#ffffff',height = 2, width = 20, padx = 80 , font = ('Sans','10','bold'), command  =Inputfun)
button1.place(x=150, y=50)
path1 = Label(root, text="")
path1.place(x=50, y=100,height = 20, width = 500)
filename1 = StringVar()
text1 = Entry(root, textvariable = filename1)
textlable1 = Label(root,text="Sheet Name:",height = 2, width = 20,padx = 80,font = ('Sans','10','bold'))
textlable1.place(x=150, y=120)
text1.place(x=230, y=170, height = 20, width = 150)
filename = StringVar()
text = Entry(root, textvariable = filename)
textlable = Label(root,text="Address Column Name:",height = 2, width = 20,padx = 80,font = ('Sans','10','bold'))
textlable.place(x=150, y=210)
text.place(x=230, y=250, height = 20, width = 150)
button3 = Button(root, text="Output Folder Location",bg='#0052cc', fg='#ffffff',height = 2, width = 20,font = ('Sans','10','bold'),padx = 80, command  =savefile)
button3.place(x=150, y=320)
path3 = Label(root, text="")
path3.place(x=50, y=370,height = 20, width = 500)
button4 = Button(root, text="Run",bg='#0052cc', fg='#ffffff',height = 2, width = 20,padx = 80,font = ('Sans','10','bold'), command  =run)
button4.place(x=150, y=480)
endtxt = Label(root, text="",height = 2, width = 20,padx = 80,font = ('Sans','10','bold'))
endtxt.place(x=150, y=530)


root.mainloop()



et = time.time()
res = et - st
final_res = res / 60

print('Execution time:', final_res, 'minutes')

print(time.ctime())

print("Done!")














