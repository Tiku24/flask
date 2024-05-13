import sqlite3
import uuid
from datetime import date

def createTables():
    conn =sqlite3.connect("my_medicalShop.db")
    cursor=conn.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR(255),
    password VARCHAR(255),
    Level INT,
    DateOfAccountCreation DATE,
    approved BOOLEAN,
    Block BOOLEAN,
    name VARCHAR(255),
    Address VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    PinCode VARCHAR(255)
);
''')
    
    #create product tables
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    Product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    price FLOAT,
    category VARCHAR(255),
    stock INTEGER,
    isActive BOOLEAN              
);
''')
    

    conn.commit()
    conn.close()
    
def createUser(name,password,Address,Email,Phone,PinCode):
    try:
        conn =sqlite3.connect("my_medicalShop.db")
        cursor=conn.cursor()
        user_id = str(uuid.uuid4()) #id will generate randomely
        dateOfCreation=date.today()

    
        cursor.execute("""INSERT INTO User(user_id, password, Level, DateOfAccountCreation, approved, Block, name, Address,email, phone, PinCode)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(user_id,password,-1,dateOfCreation,0,0,name,Address,Email,Phone,PinCode))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return False
    
