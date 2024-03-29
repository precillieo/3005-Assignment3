import psycopg2 

#Initialize Connection to the Database
DB_NAME = "University"
DB_USER = "postgres"
DB_PASSWORD = "****"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
    """Connects to the PostgreSQL database"""
    try: 
        connection = psycopg2.connect(
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT
        )
        return connection
    except Exception as e:
        print("Connection Error: ", e)
        return None
    
def getAllStudents():
    """Retrieves and displays all student records"""
    connection = connect_db()
    if connection:
        try: 
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            for student in students:
                print(student)
            connection.commit()
        except Exception as e:
            print("Error retrieving students: ", e)
        finally:
            connection.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record"""
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                           INSERT INTO students (first_name, last_name, email, enrollment_date) 
                           VALUES (%s, %s, %s, %s)""", (first_name, last_name, email, enrollment_date))
            connection.commit()
            print("Student added successfully")
        except Exception as e:
            print("Error adding student: ", e)
        finally:
            connection.close()

def updateStudent(student_id, new_email):
    """Updates the email address for a student"""
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                           UPDATE students 
                           SET email = %s
                           WHERE student_id = %s""", (new_email, student_id))
            connection.commit()
            print("Student updated successfully")
        except Exception as e:
            print("Error updating student: ", e)
        finally:
            connection.close()

def deleteStudent(student_id):
    """Deletes a student record"""
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                           DELETE FROM students
                           WHERE student_id = %s""", (student_id,))
            connection.commit()
            print("Student deleted successfully")
        except Exception as e:
            print("Error deleting student: ", e)
        finally:
            connection.close()

# To test the functions
#getAllStudents()
# addStudent("Precious", "Kolawole", "pk@example.com", "2021-09-01")
updateStudent(1, "john.doe@example.com")
#deleteStudent(4)

