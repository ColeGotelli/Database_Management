Cole Gotelli

2268217

CPSC 408-01

Assignment 3

CSV to Database:

These programs generate fake data using python's Faker library (use '''pip install Faker''' to download) to create a CSV of fake data. Then this file is parsed and inserted into a database that is also created by the program.

All the files relevant for running this assignment can be found through the path 'Assignment3/src/com/company'

Instructions for User:

1. Type 'python WriteToCSV.py' into a terminal window

2. User will be prompted to input the name of the file and the number of tuples, do so (it may take a moment to write a large number of tuples)

3. Once the csv has been create, open the Main.java program and replace 'testCSV.csv' in '''String fileName = "./testCSV.csv";''' with the name of the CSV you created

4. Next the user should run the main() function in Main.java

Notes:

This project made use of Maven's MySQL Connector

General advice and help from:
* Luke Berger
* Josh Anderson