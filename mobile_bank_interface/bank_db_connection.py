import sqlite3

con=sqlite3.connect("bank_db")
print('Connection Established')
cur = con.cursor() 
cur.executescript('drop table if exists userlogindetails;')


# user account : Accno,UserName,Password,Login_Status,FName,LName,Address,Age.
con.execute('''
   CREATE TABLE  IF NOT EXISTS userlogindetails(
    user_id INTEGER AUTO_INCREMENT,
    accno INTEGER NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL UNIQUE,
    login_status TEXT NOT NULL,
    customer_fname TEXT NOT NULL,
    customer_lname TEXT NOT NULL,
    address        TEXT NOT NULL,
    age            INTEGER NOT NULL,
    email          TEXT NOT NULL
    );
    ''')


con.execute('''
    CREATE TABLE IF NOT EXISTS account(
    accno INTEGER,
    login_status TEXT,
    balance REAL,
    btransaction TEXT,
    blimit REAL,
    t_account TEXT,
    account_status TEXT,
    ttime DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP)
    );

''')

            
cur.execute("INSERT INTO account VALUES(1,'ACTIVE',20000,'NA',2000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(2,'ACTIVE',10000,'NA',1000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(3,'ACTIVE',50000,'NA',100,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(12,'ACTIVE',50000,'NA',100,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");



cur.execute("INSERT INTO userlogindetails VALUES(100,12,'UB1234','Star1234','Active','Tulip','Spring','20 Strong road',25,'hk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(101,13,'UB1234','Star2020','Active','Yellow','Winter','23 Strong road',25,'hk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(102,14,'UB1250','Star2000','Active','Daisy','Summer','21 Strong road',55,'lk@gmail.com')");




cur.execute("SELECT * FROM userlogindetails")
rows = cur.fetchall() 

for row in rows:
    print(row)

cur.execute("SELECT * FROM account")
rows = cur.fetchall() 

for row in rows:
    print(row)
con.close()