# GeoCoding-addresses-for-Tel-Aviv-municipality
The purpose of this code is to append X Y coordinates in 2039 grid (Israel TM Grid) for an address in the city of Tel Aviv.

The Input - an Excel table that has a field of an address in Tel Aviv in Hebrew that includes a street name and a house number.
The Output - an Excel table and an SHP file of the same Input table plus fields of X Y and a and a match percentage field. 

The code is written in Python and includes the use of tkinter, arcpy and FuzzyWuzzy packages.

Before running this code, make sure that:
1. ArcGIS Pro version 2.5 or higher is installed on your computer.
2. Optional - download FuzzyWuzzy package (PIP Install). 

The code files:

1. GeoCode.py
2. Output.lyrx
3. fuzzywuzzy folder

Code steps:

1. Input an Excel table that has a Hebrew address field (street name + house number). 

2. Enter the name of the Excel sheet

3. Enter the name of the address field

4.Selecting the Output folder

5. Running the code

This is how it looks when you open the code:


![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/ae663c36-d93d-4b40-b70d-2ea35ca42eea)



For example:

![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/5bdc072a-524c-418c-8479-7539a2589d33)



