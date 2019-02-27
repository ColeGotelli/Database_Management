import sqlite3
from Students import Students
import StudentFunctions

running = True

conn = sqlite3.connect('Students.db')
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
        sub_input = 0
        while (sub_input == 0):
            sub_menu = raw_input("Enter Here: ")

            if (sub_menu == '1'):
                user_gpa = raw_input("What is the GPA you are looking for: ")
                print (StudentFunctions.selectGPA(c, user_gpa))
                sub_input = 1
            elif (sub_menu == '2'):
                user_major = raw_input("What Major are looking for: ")
                print (StudentFunctions.selectMajor(c, user_major))
                sub_input = 1
            elif (sub_menu == '3'):
                user_advisor = raw_input("Who is the Advisor you are looking for: ")
                StudentFunctions.selectAdvisor(c, user_advisor)
                sub_input = 1
            else:
                print("That was an invalid input, try again")
                sub_input = 0
    elif (option_menu == '3'):
        StudentFunctions.createStudents(c)

    elif (option_menu == '4'):
        print("Please Enter the ID of the Student you want to delete")
        user_delete = raw_input("Enter Here: ")
        StudentFunctions.deleteRecord(c, user_delete)

    elif (option_menu == '5'):
        print("Please enter the ID of the Student you want to update")
        user_ID = raw_input("Enter Here: ")
        new_major = raw_input("The new major is: ")
        new_advisor = raw_input("The new advisor is: ")
        StudentFunctions.updateStudentMajor(c, new_major, user_ID)
        StudentFunctions.updateStudentAdvisor(c, new_advisor, user_ID)

    elif (option_menu == '6'):
        print("Thanks for using the Portal. Goodbye")
        running = False

    else:
        print("That was an invalid input, try again")
        running = True

    conn.commit()