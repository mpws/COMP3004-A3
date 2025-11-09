from student_app import getAllStudents, addStudent, updateStudentEmail, deleteStudent           # Import CRUD functions from student_app


# Display all initial student records
print("Initial Students:") 
getAllStudents()


# Add new student to the database
print("Adding a new student:")
addStudent("Mike", "Pickard", "mike@example.com", "2023-09-03")
getAllStudents()


# Update existing student email
print("Update Student Mike's email:")
updateStudentEmail(4, "mike@secondexample.com")
getAllStudents()


# Delete existing student from database
print("Deleting Student Mike:")
deleteStudent(4)
getAllStudents()
