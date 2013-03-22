import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT * FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def get_project_by_title(title):
   query = """SELECT * FROM Projects WHERE title = ?"""
   DB.execute(query, (title,))
   row = DB.fetchone()
   print """\
title: %s
description: %s
max_grade: %s"""%(row[0], row[1], row[2])

def get_grade_from_grades(student, project):
    query = """SELECT * FROM GRADES WHERE student = ? AND project = ?"""
    DB.execute(query, (student, project,))
    row = DB.fetchone()
    print """\

    """

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("my_database.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects values (?, ?, ?)"""

    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s %s " % (title, description, max_grade)

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "title":
            get_project_by_title(*args)
        elif command == "new_student":
            make_new_student(*args)
        elif command == "new_project":
            make_new_project(*args)
     

    CONN.close()

if __name__ == "__main__":
    main()
