# GeoCoding-addresses-for-Tel-Aviv-municipality
The purpose of this code is to append X Y coordinates in 2039 grid (Israel TM Grid) for a text address in Tel Aviv.

The Input - an Excel table that has a field of an address in Tel Aviv that includes a street name and a house number in Hebrew.

The Output - an Excel table and SHP file of the same Input table plus fields of X Y with a match percentage field from the free API of the address layer of Tel Aviv municipality.

There are 2 options for executing the code:

   GeoCode Arcpy:
   
     -Code that includes the use of the Arcpy package of ArcGIS.
   
     - Faster
     
     - Only for ArcGIS Pro users (paid)
     
   GeoCode Open Source:
   
     -Code that includes the use of open source packages
   
     -free
     
     - About 2-4 minutes slower than Arcpy's code

Before running this code, make sure that:
1. for GeoCode Arcpy - make sure you have ArcGIS Pro version 2.5 or higher that installed on your computer.
2. Optional - download FuzzyWuzzy package (PIP Install). 

The code files:

1. GeoCode Arcpy.py
2. GeoCode Open Source.py
3. Output.lyrx
4. fuzzywuzzy folder - Not required if you already have it installed

Code steps:

1. Input an Excel table that has a Hebrew address field (street name + house number). 

2. Enter the name of the Excel sheet

3. Enter the name of the address field

5. Selecting the Output folder

7. Running the code


This is how it looks when you open the code:

![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/c87d0dfa-d959-4fd5-84dc-8bff8da9d5f5)



![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/4a10d6f0-3ed0-4c98-a868-ee9fe4299470)



For example:

![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/5bdc072a-524c-418c-8479-7539a2589d33)


At the end of the process, your Output folder will contain:

![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/6c1cb0a6-3e64-484e-be06-585e8a009c85)



![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/20ba11d2-8c48-4704-9f3a-6acce5f4e0c1)

![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/157f3d3f-0818-4bdf-87fb-18a4be7183b9)


![image](https://github.com/jonathandell27/GeoCoding-addresses-for-Tel-Aviv-municipality-by-API/assets/59395234/c6f0bb80-0f84-443a-b373-02278e9325af)








