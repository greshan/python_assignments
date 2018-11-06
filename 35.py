#35. Implement a python code for the database CRUD operations.

import mysql.connector
global conn,cursor;
conn = mysql.connector.connect(host="localhost", user="greshan",password="password")

def connection():

    if conn.is_connected():
        print("connected")
    else:
        print("Not Connected")

def database(Name):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE " + Name)
    print("Database Created :",Name)

def table(tablename, Name):
    conn_db = mysql.connector.connect(host="localhost", db=Name, user="greshan",password="password")
    mycursor = conn_db.cursor()
    mycursor.execute("CREATE TABLE "+tablename+"(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255))")
    print("Table Created :",tablename)
    conn_db.close()

def insertinto(tablename, Name):
    conn_db = mysql.connector.connect(host="localhost", db=Name, user="greshan",password="password")
    mycursor = conn_db.cursor()
    sql = "INSERT INTO "+tablename+" (id, fname, lname) VALUES (%s, %s, %s)"
    id = input("\nEnter id\n")
    fname = input("\nEnter fname\n")
    lname = input("\nEnter lname\n")

    val = (id, fname, lname)
    mycursor.execute(sql, val)
    conn_db.commit()
    print("\n Success: Insertion Successful \n")
    conn_db.close()


def main():
    while True:


        print("Enter your choice:: ")
        print("Create database - 1: ")
        print("Create table - 2: ")
        print("Insert values - 3: ")
        print("Quit- q: ")

        choice = input("Enter the option: ")


        if choice == '1':
            inp = input("Enter new db name: ")
            database(inp)

        if choice == '2':
            inp = input("Enter db name: ")
            inp1 = input("Enter table name: ")
            table(inp1, inp)

        if choice == '3':
            inp = input("Enter db name: ")
            inp1 = input("Enter table name in: ")
            insertinto(inp1, inp)

        if choice == 'q':
            sys.exit()




if __name__ == "__main__":
    main();
