# DBMS_PROJECT
BLOOD DONATION MANAGEMENT SYSTEM
Blood donation management system aims at storing data of a blood bank and performing CRUD operations on the same.
The main goal of the system is to project blood bank as well as donor data. The project is entirely administrative.
The database contains many entities:
Donor
Blood
Blood bank
Hospital
Blood bank manager
Receptionist
FRONTEND USED:
STREAMLIT APP IS USED TO CREATE FRONTEND IN PYTHON
BACKEND:
MYSQL (TABLES CREATED AND POPULATED :THE CSV FILES USED TO POPULATE THE DATABASE NEED TO BE STORED IN THE SAME DATABASE FILE IN THE XAMPP/MYSQL/DATA FOLDER , OTHERWISE THE LOAD DATA INFILE QUERIES WONT RUN)
THE FRONTEND AND THE BACKEND ARE CONNECTED USING THE MYSQL CONNECTOR
import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
database="DBMS_PROJECT_PES1UG20CS097"
)
c = mydb.cursor()
PLATFORM USED: VS CODE
The code, csv files ,the report and the sql file containing all the ddl statemnets and queries are shared in the folder.
