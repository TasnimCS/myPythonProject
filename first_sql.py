import sqlite3
import os


def employeedata():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    query = ''' CREATE TABLE Employee ( EmpID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Salary REAL, Address TEXT)'''

    cur.execute(query)
    con.commit()
    con.close()

def addemployee():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()
    insert1 = ''' INSERT INTO Employee VALUES ( ?, ?, ?, ?) '''

    cur.execute(insert1)
    con.commit()
    con.close()

def updateemployee():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()

    cur.execute(' UPDATE Employee SET EmpID=?, Name=?, Salary=?, Address= ? WHERE EmpID = ?')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:30 {row[0]:5}}')

    con.commit()
    con.close()

def deletemployee():
    con = sqlite3.connect("Employee.db")
    cur = con.cursor()

    cur.execute( 'DELETE FROM Employee EmpID=?, Name=?, Salary=?, Address= ? WHERE EmpID = ?')
    con.commit()
    con.close()
