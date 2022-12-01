import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="DBMS_PROJECT_PES1UG20CS097"
)
c = mydb.cursor()



# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS TRAIN(emp_id TEXT,name TEXT, email TEXT, ph_no TEXT)')


def add_data_manager(eid,name,email,phno):
    c.execute('INSERT INTO blood_bank_manager VALUES (%s,%s,%s,'
              '%s)',
              (eid,name,email,phno))
    mydb.commit()
def add_data_donor(DID,name,gender,DOB,Ph_no,state,city,pin,recomm_id,receptionist_emp_id):
    c.execute(f'INSERT INTO Donor VALUES {DID,name,gender,DOB,Ph_no,state,city,pin,recomm_id,receptionist_emp_id}')
              
              
    mydb.commit()

def  add_data_blood_bank(B_No,services,timings,MGR_emp_id):
    c.execute(f'INSERT INTO blood_bank VALUES {B_No,services,timings,MGR_emp_id}')
    mydb.commit()
def view_all_data_manager():
    c.execute('SELECT * FROM blood_bank_manager')
    
    data = c.fetchall()
    return data
def view_all_data_donor():
    c.execute('SELECT * FROM Donor')
    
    data = c.fetchall()
    return data

def view_all_data_blood_bank(): 
    c.execute('SELECT * FROM blood_bank')
    
    data = c.fetchall()
    return data
   



def edit_dealer_data(emp_id,email):
    c.execute("UPDATE blood_bank_manager SET email=%s WHERE "
              "emp_id=%s", (email,emp_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(eid):
    c.execute('DELETE FROM blood_bank_manager WHERE emp_id="{}"'.format(eid))
    mydb.commit()

def query(q):
    
        c.execute(q)
        return c.fetchall()
def donor(q):
    c.execute(f"SELECT Donor.DID,Donor.name,Donor.ph_no FROM blood JOIN Donor ON Donor.DID=blood.DID     where blood.type='{q}'")
    return c.fetchall()

