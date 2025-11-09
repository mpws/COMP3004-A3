import psycopg2                                                             # PostgreSQL interaction import
from db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT       # Credentials from config file


def connect():                                                              # Connection to PostgreSQL database using the credentials                          
    return psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST, port = DB_PORT)


def getAllStudents():                                                       # Display all student records
    con = connect()                                                         # Open connection to database
    cur = con.cursor()                                                      # Create cursor to execute SQL
    cur.execute("SELECT * FROM students;")                                  # Run query
    rows = cur.fetchall()                                                   # Fetch and print results
    for row in rows:
        print(row)
    cur.close()                                                             # Close cursor
    con.close()                                                             # Close the connection


def addStudent(first_name, last_name, email, enrollment_date):              # Add a new student to the database
    con = connect()
    cur = con.cursor()
    cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s); """, (first_name, last_name, email, enrollment_date))
    con.commit()
    cur.close()
    con.close()


def updateStudentEmail(student_id, new_email):                              # Update existing student email
    con = connect()
    cur = con.cursor()
    cur.execute("""UPDATE students SET email = %s WHERE student_id = %s; """, (new_email, student_id))
    con.commit()
    cur.close()
    con.close()


def deleteStudent(student_id):                                              # Delete existing student from database
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    con.commit()
    cur.close()
    con.close()