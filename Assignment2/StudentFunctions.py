import sqlite3
from Student import Student

class StudentFunctions:

    def selectEverything(c):
        c.execute("select * from Students")
        all_rows = c.fetchall()

    def selectMajor(c, user_major):
        c.execute("select * from Students WHERE Major = ?", (user_major,))
        all_rows = c.fetchall()

    def selectGPA(c, user_gpa):
        c.execute("select * from Students WHERE GPA = ?", (user_gpa,))
        all_rows = c.fetchall()

    def selectAdvisor(c, user_advisor):
        c.execute("select * from Students WHERE FacultyAdvisor = ?", (user_advisor,))
        all_rows = c.fetchall()

    def createStudents(c):
        fName = raw_input("Enter Student First Name: ")
        lName = raw_input("Enter Student Last Name: ")
        major = raw_input("Enter Major: ")
        gpa = raw_input("Enter Student GPA: ")
        advisor = raw_input("Enter Faculty Advisor: ")

        stu = Student(fName, lName, major, gpa, advisor)

        c.execute("INSERT INTO students('FirstName', 'LastName', 'Major', 'GPA', 'FacultyAdvisor')"
                  "VALUES (?, ?, ?, ?, ?)", stu.student_info())

    def deleteRecord(c, user_delete):
        c.execute("delete from Students where StudentID = " + user_delete)
        all_rows = c.fetchall()

    def updateStudent(c, new_major, new_advisor):
        c.execute("update Students set Major = ?", (new_major,))
        all_rows = c.fetchall()
        c.execute("update Students set FacultyAdvisor = ?", (new_advisor,))
        all_rows = c.fetchall()