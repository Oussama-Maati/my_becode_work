import mysql.connector


def init_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="oussama",
        password="becode"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS becode;"
                     "USE becode;"
                     "CREATE TABLE IF NOT EXISTS contact_form ( "
                     "id INT AUTO_INCREMENT PRIMARY KEY, "
                     "first_name VARCHAR(255) NOT NULL, "
                     "last_name VARCHAR(255) NOT NULL, "
                     "email VARCHAR(255) NOT NULL, "
                     "country VARCHAR(255) NOT NULL, "
                     "message TEXT NOT NULL, "
                     "gender ENUM('Male', 'Female') NOT NULL, "
                     "topics VARCHAR(255) NOT NULL "
                     ");")


def send_db(values):
    mydb = mysql.connector.connect(
        host="localhost",
        user="oussama",
        password="becode"
    )
    mycursor = mydb.cursor()
    mycursor.execute("use becode;")
    sql = "INSERT INTO contact_form (first_name, last_name, email, country, message, gender, topics) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, values)
    mydb.commit()
