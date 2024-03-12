import psycopg

# Will continually prompt the user to select an option until they exit.
def main():
    connect()
    
    while True:
        print("\nOptions")
        print("1. Get all student records")
        print("2. Add a student")
        print("3. Update a student email")
        print("4. Delete a student")
        print("5. Exit\n")
        
        option = input("Enter your selection: ").strip()

        # Get all students
        if option == "1":   
            print("All student records:")
            getAllStudents()
        # Add a student
        elif option == "2":
            first_name = input("Enter student's first name: ").strip()
            last_name = input("Enter student's last name: ").strip()
            email = input("Enter student's email: ").strip()
            enrollment_date = input("Enter student's enrollment_date[YYYY-MM-DD]: ").strip()

            addStudent(first_name, last_name, email, enrollment_date)
            print("Student successfully added.")
        # Update a student's email
        elif option == "3":
            student_id = input("Enter student's id: ").strip()
            new_email = input("Enter student's new email: ").strip()

            updateStudentEmail(student_id, new_email)
            print("Student's email successfully updated.")
        # Delete a student
        elif option == "4":
            student_id = input("Enter student's id: ").strip()

            deleteStudent(student_id)
            print("Student successfully deleted.")
        # Exit program
        elif option == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

    conn.close()

# Will attempt to establish a connection to the database
def connect():
    global conn 
    try:
        conn = psycopg.connect(
            dbname="a3_student_db", user="postgres",
            password="postgres", host="localhost"
        )
        return conn
    except psycopg.OperationalError as e :
        print(f"Error: {e}")
        exit(1)


# To view every row from the students table. Each row will be printed to the screen.
def getAllStudents():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        cursor.close()
    except psycopg.OperationalError as e :
            print(f"Error: {e}")
            exit(1)

# To add a new student to the database.
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        conn.commit()
        cursor.close()
    except psycopg.OperationalError as e :
            print(f"Error: {e}")
            exit(1)

# To update a student's email. Must know the student id.
def updateStudentEmail(student_id, new_email):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()
        cursor.close()
    except psycopg.OperationalError as e :
            print(f"Error: {e}")
            exit(1)

# To remove a student from the database. Must know the student id.
def deleteStudent(student_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        cursor.close()
    except psycopg.OperationalError as e :
            print(f"Error: {e}")
            exit(1)

if __name__ == "__main__":
    main()
