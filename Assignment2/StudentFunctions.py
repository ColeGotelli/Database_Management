import sqlite3
from Students import Students

def selectEverything(c):
    c.execute("select * from Student")
    all_rows = c.fetchall()
    print(all_rows)

def selectMajor(c, user_major):
    c.execute("select * from Student WHERE Major = ?", (user_major,))
    all_rows = c.fetchall()
    print(all_rows)

def selectGPA(c, user_gpa):
    c.execute("select * from Student WHERE GPA = ?", (user_gpa,))
    all_rows = c.fetchall()
    print(all_rows)

def selectAdvisor(c, user_advisor):
    c.execute("select * from Student WHERE FacultyAdvisor = ?", (user_advisor,))
    all_rows = c.fetchall()
    print(all_rows)

def createStudents(c):
    fName = raw_input("Enter Student First Name: ")
    lName = raw_input("Enter Student Last Name: ")
    major = raw_input("Enter Major: ")
    gpa = raw_input("Enter Student GPA: ")
    advisor = raw_input("Enter Faculty Advisor: ")

    stu = Students(fName, lName, major, gpa, advisor)

    c.execute("INSERT INTO Student('FirstName', 'LastName', 'Major', 'GPA', 'FacultyAdvisor')"
              "VALUES (?, ?, ?, ?, ?)", stu.student_info())

def deleteRecord(c, user_delete):
    c.execute("delete from Student where StudentID = " + user_delete)
    all_rows = c.fetchall()
    print(all_rows)

def updateStudentMajor(c, new_major, stuID):
    c.execute("update Student set Major = ? where StudentID = ?", (new_major, stuID,))
    all_rows = c.fetchall()
    print(all_rows)

def updateStudentAdvisor(c, new_advisor, stuID):
    c.execute("update Student set FacultyAdvisor = ? where StudentID = ?", (new_advisor, stuID,))
    all_rows = c.fetchall()
    print(all_rows)