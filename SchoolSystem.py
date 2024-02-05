# Group Tutor Project by Max Croft

import sqlite3
import random
from faker import Faker
conn = sqlite3.connect("student.db")
curr = conn.cursor()
fake = Faker()



def generatedata():
    for i in range(2000):
        num = random.randint(0, 1)
        studentid = str(random.randint(0, 10000000))
        firstname = fake.first_name()
        surname = fake.last_name()
        age = fake.date_of_birth()
        home_address = fake.address()
        home_phone_number = fake.phone_number()
        tutor_group = "TUTOR_" + str(random.randint(1, 5))
        if num == 0:
            gender = "Male"
        else:
            gender = "Female"
        curr.execute("INSERT INTO Students (student_id, forename, surname, date_of_birth, home_address, home_phone_number, tutor_group, gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (studentid, firstname, surname, age, home_address, home_phone_number, tutor_group, gender))
        conn.commit()



def menu(user):
    print("Welcome " + user[1] + " to Tree Road School." + " Please select an option below.")
    print("1. View Student Details")
    print("2. Add Student")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Generate Report")
    choice = input("Choice: ")
    if choice == "1":
        viewstudentdetails(user)
    elif choice == "2":
        createstudent(user)
    elif choice == "3":
        editstudent(user)
    elif choice == "4":
        deletestudent(user)
    elif choice == "5":
        generatereport(user)
    else:
        print("Invalid Choice. Please try again")
        menu(user)

def login():
    attempts = 0
    if attempts == 3:
        print("You cannot login due to too many wrong attempts. Please try again later.")
    print("Welcome to the School System")
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    curr.execute("SELECT * FROM Staff WHERE username = ? AND password = ?", (username, password))
    rows = curr.fetchall()
    if len(rows) == 0:  # Check if rows list is empty
        print("No Login Found. Please try again")
        attempts = attempts + 1
        login()
    else:  
        if username == rows[0][3] and password == rows[0][4]:
            print("Login Successful")
            user = rows[0]
            menu(user)
          
        else:
            print("Login Failed. Please try again")
            attempts = attempts + 1
            login()


# This function is not accessable unless code is edited directly to add it =
def createstafflogin():
    print("Create Staff Login")
    print("Please enter your details below")
    firstname = input("First Name: ")
    surname = input("Surname: ")
    username = input("Username: ")
    password = input("Password: ")
    staffid = str(random.randint(1000, 9999))
    curr.execute("INSERT INTO Staff (StaffID, FirstName, LastName, Username, Password) VALUES (?, ?, ?, ?, ?)", (staffid, firstname, surname, username, password))
    conn.commit()
    print("Login Created Successfully")

# Creates a student
def createstudent(user):
    print("Create A Student")
    print("Please enter the student details below: ")
    firstname = input("First Name: ")
    surname = input("Surname: ")
    age = input("Date of Birth: ")
    home_address = input("Home Address: ")
    home_phone_number = input("Home Phone Number: ")
    gender = input("Gender: ")
    studentid = str(random.randint(1000, 9999))
    tutor_group = input("Tutor Group: ")
    curr.execute("INSERT INTO Students (student_id, surname, date_of_birth, home_address, home_phone_number, gender, tutor_group) VALUES (?, ?, ?, ?, ?, ?, ?)", (studentid, firstname, surname, age, home_address, home_phone_number, gender, tutor_group))   
    conn.commit()
    print("Student Created Successfully")


# Edit Student (This will let admins edit student detals)
def editstudent(user):
    print("Edit Student")
    print("Please enter the student details below: ")
    change = input("What would you like to change? ")
    if change == "First Name":
        firstname = input("First Name: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET firstname = ? WHERE student_id = ?", (firstname, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Surname":
        surname = input("Surname: ") 
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET surname = ? WHERE student_id = ?", (surname, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Date of Birth":
        age = input("Date of Birth: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET date_of_birth = ? WHERE student_id = ?", (age, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Home Address":
        home_address = input("Home Address: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET home_address = ? WHERE student_id = ?", (home_address, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Home Phone Number":
        home_phone_number = input("Home Phone Number: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET home_phone_number = ? WHERE student_id = ?", (home_phone_number, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Gender":
        gender = input("Please enter the new gender: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET gender = ? WHERE student_id = ?", (gender, studentid))
        conn.commit()
        print("Student Updated Successfully")
    elif change == "Tutor Group":
        tutor_group = input("Tutor Group: ")
        studentid = input("Student ID: ")
        curr.execute("UPDATE Students SET tutor_group = ? WHERE student_id = ?", (tutor_group, studentid))
        conn.commit()
        print("Student Updated Successfully")
    else:
        print("Invalid Choice. Please try again")
        editstudent(user)

# Search for a student 
def viewstudentdetails(user):
    search = input("Search By: ")
    student = input("Search Quary: ")
    curr.execute(f"SELECT * FROM Students WHERE {search} = ?", (student,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No Student Found. Please try again")
        viewstudentdetails(user)
    else:
        # print each row that has got found
        for row in rows:
            print("Student Details")
            print("=====================================")
            print("Student ID: " + str(row[0]))
            print("First Name: " + row[1])
            print("Surname: " + row[2])
            print("Date of Birth: " + row[3])
            print("Home Address: " + row[4])
            print("Home Phone Number: " + row[5])
            print("Gender: " + row[6])
            print("Tutor Group: " + row[7])
            print("=====================================")

# Delete a student from the system
def deletestudent(user):
    print("Delete A Student") 
    search = input("Search By: ")
    student = input("Search Quary: ")
    curr.execute(f"SELECT * FROM Students WHERE {search} = ?", (student,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No Student Found. Please try again")
        deletestudent()
    else:
        print("Student Name: " + rows[0][1] + " " + rows[0][2])
        warning = input("Are you sure you want to delete this student? (Y/N): ")
        if warning == "Y":
            curr.execute(f"DELETE FROM Students WHERE {search} = ?", (student,))
            conn.commit()
            print("Student Deleted Successfully")
        elif warning == "N":
            print("Student Not Deleted")
        else:
            print("Invalid Choice. Please try again")
            deletestudent()


# Generate a report for parents on a student
def generatereport(user):
    print("Generate Report")
    student = input("Student ID: ")
    # get the student details
    curr.execute("SELECT * FROM Students WHERE student_id = ?", (student,))
    rows = curr.fetchall()
    if len(rows) == 0:
        print("No Student Found. Please try again")
        generatereport(user)
    else:
        studentinfo = rows[0]
    tests = input("How many tests has the student taken? ")
    results = []
    for i in range(int(tests)):
        test = input("Test Name: ")
        mark = input("Test Mark: ")
        studentid = "None"
        results.append((test, mark, studentid))
    file = open("report.txt", "w")
    file.write("Student Report")
    file.write("\n")
    file.write("=====================================")
    file.write("Student ID: " , str(studentinfo[0]))
    file.write("Studnet Name: " + studentinfo[1] + " " + studentinfo[2])
    file.write("Date of Birth: " + studentinfo[3])
    file.write("Home Address: " + studentinfo[4])
    file.write("Home Phone Number: " + studentinfo[5])
    file.write("Student Gender: " + studentinfo[6])
    file.write("Tutor Group: " + studentinfo[7])
    file.write("\n")
    # write a line for each test
    for test, mark, studentid in results:
        file.write("=====================================")
        file.write("\n")
        file.write("Test Name: " + test)
        file.write("\n")
        file.write("Test Grade: " + mark)
        file.write("\n")
    file.write("=====================================")
    file.write("\n")
    file.close()
    print("Report Generated Successfully")


login()
