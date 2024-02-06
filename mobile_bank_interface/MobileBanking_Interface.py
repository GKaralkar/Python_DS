# Mobile Banking Interface
import sqlite3



loginname=""
lpassword=""
accountno=""

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
con.commit()
            
cur.execute("INSERT INTO account VALUES(12,'ACTIVE',20000,'NA',2000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(2,'ACTIVE',10000,'NA',1000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(3,'ACTIVE',50000,'NA',100,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");



cur.execute("INSERT INTO userlogindetails VALUES(100,12,'UB1234','Star1234','Active','Tulip','Spring','20 Strong road',25,'hk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(101,13,'UB1234','Star2020','Active','Yellow','Winter','23 Strong road',25,'hk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(102,14,'UB1250','Star2000','Active','Daisy','Summer','21 Strong road',55,'lk@gmail.com')");


con.commit()

#cur.execute("SELECT * FROM userlogindetails")
#rows = cur.fetchall() 

#for row in rows:
   # print(row)

#cur.execute("SELECT * FROM account")
#rows = cur.fetchall() 

#for row in rows:
  #  print(row)

# user account : Accno,UserName,Password,Login_Status,FName,LName,Address,Age.



    
#Account : Accno,Balance,Account_type,Account_Status

# list
#Transaction_type=['Transferring Funds','Depositing Money','Funds Withdrawal']

def view_account_details(accountno):

    #print(f"Account No :{}")
   # print(f"Account Type:{}")
    accno=int(accountno) 

    cur.execute("SELECT * FROM account WHERE accno = ?",(accno,))
   
    rows = cur.fetchone() 

    for row in rows:
        print(row)

    

#def  user_option_menu():
    
    #choice=input('\n\n Enter your choice : \n\n 1. View Balance  :\n\n 2. Funds Withdrawal :'+
               # ' \n\n 3.Transferring Funds  :\n\n 4.Depositing Money  '
                # +' \n\n 5. Exit the program :')

        #if choice=='1':
        # def account_info(account_no):
         #def view_Balance(account_no):
         #def update_account_details():

    # elif choice=='2':
        # def account_info(account_no):
         #def withdrawal_funds(accountno):
        #def update_account_details():
     #elif choice=='3':
        #def transferring_funds(accountno)
        #def update_account_details():
    #elif choice=='4':
        #def deposit_funds(accountno):
        #def update_account_details():
        

    #elif choice=='5':
     #sys.exit(0)

def user_login():

    loginname=input("Enter the user name :")
    lpassword=input("Enter the password  :")
    
    #query = "SELECT username,password FROM userlogindetails WHERE username =%s AND password =%s"
    #cur.execute(query,(loginname,lpassword))
    
    query=cur.execute("SELECT username, password FROM userlogindetails WHERE username = ? AND password = ?", (loginname, lpassword))

    #query=cur.execute("SELECT username,password FROM userlogindetails WHERE username=? AND password=?, (str(loginname),str(lpassword))");
    
    if (len(query.fetchall()) > 0):
    
       print("Welcome")
       account_info(loginname,lpassword)
    else:
       print("Incorrect login name and password.. ")
    # look up login name and lpassword
    #FOR block to get account details
    
    #account_info(account_no):
    

def withdrawal_funds(accountno):
 #   accountinfo(accountno)
    wamount=float(input("Please enter the amount to be withdrawn"))
    acc_balance=0
  
     
    cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,))
   
    acc_balance=float(cur.fetchone()[0])
    print(acc_balance)

    acc_bal=float(acc_balance)-float(wamount)
    cur.execute("SELECT * FROM account WHERE accno = ?",(accountno,))
    cur.execute("UPDATE account set balance = ? where accno = ? ",(acc_bal,accountno,))
    con.commit()
     #validation code block for wamount
    # FOR block to get the balance - account no and subtract the amount from the balance)
    # Update the account_details and Update the balance...

def transferring_funds(accountno):
   
   acc_balance=0
   
   tamount=float(input("Enter the amount to be transferred :"))
   
   accno=int(accountno) 
  
  # cur.execute("SELECT * FROM account WHERE accno = ?",(accno,))
   
   #rows = cur.fetchall() 

   #for row in rows:
       # print(row)

   
   cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,))
   
   acc_balance=float(cur.fetchone()[0])
   
   print(f"The chosen account Balance = {acc_balance}")
   
   acc_bal=float(acc_balance)-float(tamount)
   
   cur.execute("SELECT * FROM account WHERE accno = ?",(accountno,))
   
   

   taccountno=int(input("Enter the account number to which the funds have to be transferred to... "))
   
   cur.execute("SELECT balance FROM account WHERE accno =? ", (taccountno,))
   

   tacc_balance=float(cur.fetchone()[0])
   print(tacc_balance)
   
   tacc_bal=float(tacc_balance)+float(tamount)

   cur.execute("SELECT * FROM account WHERE accno = ?",(taccountno,))

   cur.execute("UPDATE account set balance = ? where accno = ? ",(acc_bal,accountno,))
   
   cur.execute("UPDATE account set balance = ? where accno = ? ",(tacc_bal,taccountno,))
   

   cur.execute("SELECT * FROM account WHERE accno = ?",(taccountno,))
   rows = cur.fetchone() 
   for row in rows:
        print(row)
  
   # Update the account_details and Update the balance...
   
   #call to function  def view_Balance(account_no):

def deposit_funds(accountno):
   #accountinfo(acountno)
    
    damount=float(input("Please enter the amount to be deposited"))
    acc_balance=0
   
    accno=int(accountno) 

    #cur.execute("SELECT * FROM account WHERE accno = ?",(accno,))
   
    #rows = cur.fetchall() 

    #for row in rows:
      #  print(row)

   
    cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,))
   
    acc_balance=float(cur.fetchone()[0])
    print(acc_balance)
    acc_bal=float(acc_balance)+float(damount)
    print(acc_bal)
    cur.execute("UPDATE account set balance = ? where accno = ? ",(acc_bal,accountno,))
    
    accno=int(accountno) 

    cur.execute("SELECT * FROM account WHERE accno = ?",(accno,))
   
    rows = cur.fetchone() 

    for row in rows:
        print(row)


con.commit()
    # FOR block to get the balance - account no and add the amount from the balance)
    #nBalance=balance+damount

#def update_account_details(accountno):
    #cur.execute("UPDATE Product set StockLevel = ? where ProductID = ?",(Stock_Update,Product_ID))
    # update the account_details   #accountno="AC1234"
   # if str(accountno)==account_details.get("accountno")):
        #print(account_details.get(str(accountno)))

#account_details={"accountno":"AC1234","Balance":'£10000',"Account_type":'NA',"Limit":'£2000',"Account_type":'Saving',"Account_Status":'Active'}
#accountno="AC1234"

#print(account_details.get("accountno"))


#key=accountno
                               
#for key in account_details.keys():
	
  #  if account_details.get[key]=="AC1234":
    	
       #  val=str(float(account_details.get['Balance'])-100)
			
            
        #account_details = {**account_details,'Balance':str(val)}
            
#print(account_details)
def account_info(lname,lpassword):
    cur.execute("SELECT * FROM userlogindetails WHERE username = ? AND password = ? ", (lname, lpassword))
    rows = cur.fetchall() 

    for row in rows:
        print(row)

       
def main():

       # user_login()
        
        loginname='UB1234'
        lpassword='Star1234'

        cur.execute("SELECT accno FROM userlogindetails WHERE username = ? AND password = ? ", (loginname,lpassword))
        
        accountno=int(cur.fetchone()[0])
        print(str(accountno))
        
        transferring_funds(accountno)
        print("Transferring Funds...")
        view_account_details(accountno)

        deposit_funds(accountno)
        print("Deposit Funds....")
        view_account_details(accountno)
        
        withdrawal_funds(accountno)
        print("After withdrawal...")
        view_account_details(accountno)
        


       
main()
