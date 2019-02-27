import sqlite3
from Student import Student
import StudentFunctions

running = True

conn = sqlite3.connect('Students.db.sqlite')
c = conn.cursor()

print ("Welcome to the Portal")
print ("Please type the number of the action you want to perform, then press enter")
print ("1: Display all the Students in the Database")
print ("2: Choose a Student based on their GPA, Major, or Advisor")
print ("3: Add a Student to the Database")
print ("4: Delete a Student from the Database")
print ("5: Change a Students Major or Advisor")
print ("6: Exit the Portal")

while(running):
    print("Please enter an Option")
    option_menu = raw_input()

    if (option_menu == '1'):
        print("Here is the Entire Student Database")
        StudentFunctions.selectEverything(c)

    elif (option_menu == '2'):
        print("To choose a student by GPA press 1")
        print("To choose a student by Major press 2")
        print("To choose a student by Advisor press 3")
        sub_menu = raw_input("Enter Here: ")

    elif (option_menu == '6'):
        print("Thanks for using the Portal. Goodbye")
        running = False

