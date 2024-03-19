import psycopg2 

#Initialize Connection to the Database
DB_NAME = "University"
DB_USER = "postgres"
DB_PASSWORD = "Oluwakemi@666"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_db():
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
    
#quick test
connection = connect_db()
if connection:
    print("Connection Successful")
else:
    print("Connection Failed")

