# Mobile Banking Interface
import sqlite3
import sys
import datetime
import re

loginname=''
lpassword=''
accountno=999


#_________________________________________ SQLITE TABLE - DUMMY DATA_________________________________________________________________

con=sqlite3.connect("bank_db")

print('\n Connection Established')

cur = con.cursor() 

cur.executescript('drop table if exists userlogindetails;')

cur.executescript('drop table if exists account;')

cur.executescript('drop table if exists acc_transaction;')

# user account : Accno,UserName,Password,Login_Status,FName,LName,Address,Age.
con.execute('''
   CREATE TABLE  IF NOT EXISTS userlogindetails(
    user_id INTEGER AUTO_INCREMENT,
    accno    INTEGER NOT NULL PRIMARY KEY,
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
    blimit REAL,
    t_account TEXT,
    account_status TEXT,
    ttime DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP)
    );

''')




con.execute('''
    CREATE TABLE IF NOT EXISTS acc_transaction(
    accno INTEGER,
    balance REAL,
    blimit REAL,
    t_account TEXT,
    b_transaction TEXT,
    account_status TEXT,
    ttime DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP)
    );

''')


            
cur.execute("INSERT INTO account VALUES(12,'ACTIVE',20000,2000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(2,'ACTIVE',10000,1500,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");
cur.execute("INSERT INTO account VALUES(10,'ACTIVE',50000,1000,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");

cur.execute("INSERT INTO account VALUES(14,'ACTIVE',30000,1200,'BALANCE','ACTIVE',CURRENT_TIMESTAMP)");

cur.execute("INSERT INTO userlogindetails VALUES(100,12,'UB1234','Star1234','Active','Tulip','Spring','20 Strand road',25,'hk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(101,10,'UB1244','Star2020','Active','Yellow','Winter','23 Storm road',25,'hsg@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(102,2,'UB1250','Star2030','Active','Daisy','Summer','21 Strong road',55,'lk@gmail.com')");
cur.execute("INSERT INTO userlogindetails VALUES(102,14,'UB1250','Star2000','Active','Orchid','Autumn','21 Green road',55,'lk@gmail.com')");




con.commit()

#_________________________________________ SQLITE TABLE - SQL QUERIES_________________________________________________________________


def view_account_details(accountno):

    accno=int(accountno)
    
    print(f"ACCOUNT DETAILS  - ACCOUNT NO : {accno}  ")

    cur.execute("SELECT balance FROM account WHERE accno = ?",(accno,))
   
    rows = cur.fetchone() 

    for row in rows:
        print(f" BALANCE £ : {row}")

    


def  user_option_menu(accountno):
      
        
    
        choice=input('\n\n Enter your choice : \n\n 1. View Balance \n\n 2. Funds Withdrawal '+
                             ' \n\n 3.Transferring Funds \n\n 4.Depositing Money  '+' \n\n 5. Exit the program :')

        if choice=='1':

           view_account_details(accountno)
           user_option_menu(accountno)
        
        elif choice=='2':
                  withdrawal_funds(accountno)
                  user_option_menu(accountno)
        elif choice=='3':
                  transferring_funds(accountno)
                  user_option_menu(accountno)
        elif choice=='4':
                  deposit_funds(accountno)
                  user_option_menu(accountno)
        else:
                  sys.exit(0)
           

def user_login():
    

    loginname=input("Enter the user name :")

    lpassword=input("Enter the password  :")
    
  
    
    query=cur.execute("SELECT username, password FROM userlogindetails WHERE username = ? AND password = ?", (loginname, lpassword))

   
    
    if (len(query.fetchall()) > 0):
    
       print(" Welcome : ")
       
       account_info(loginname,lpassword)

    else:

       print("Incorrect login name and password.. ")
    

def withdrawal_funds(accountno):    # withdrawal of funds 
 
    acc_balance=0
  
     
    cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,))
   
    acc_balance=float(cur.fetchone()[0])



    print(f"ACCOUNT DETAILS : Account no - {accountno}  Account Balance £ :  {acc_balance}")
  

  

    flag=False

    while flag==False:

       wamount=input("Please enter the amount to be withdrawn £ :")
   
      

       if  validate_value(wamount)==True:
    
           accno=int(accountno)

           flag=True





   
    wamount=float(wamount)
    
    cur.execute("SELECT blimit FROM account WHERE accno =? ", (accountno,))
   
    blimit=float(cur.fetchone()[0])
    

    
    if (acc_balance-wamount) >= blimit :  # Update the account_details and Update the balance...

        acc_bal=float(acc_balance)-float(wamount)

        

        cur.execute("UPDATE account set balance = ? , ttime=CURRENT_TIMESTAMP  where accno = ? ",(acc_bal,accountno,))

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
        cur.execute("INSERT into  acc_transaction (accno,balance,blimit,t_account,b_transaction,account_status,ttime) values(?,?,?,?,?,?,?)" ,(accountno,acc_bal,blimit,accountno,'Withdraw Funds','ACTIVE',now))
    
    else :
        
        print(f" WITHDRAWAL TRANSACTION DENIED BALANCE BELOW ACCOUNT MIN LIMIT i.e. £{blimit} ....")


    transaction_history(accountno)

    con.commit()
    
     #validation code block for wamount
    
def transferring_funds(accountno):    # Transferring Funds 
   
   acc_balance=0
   
   print(f" Account no : {accountno} ")

   flag=False

   while flag==False:
   
       tamount=input("\n Please enter the amount to be transferred  £ :")     # Amount to be transferred

       if  validate_value(tamount)==True:
    
           accno=int(accountno)

           flag=True
   
   
   cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,)) # query to fetch the balance of Account A 
   
   acc_balance=float(cur.fetchone()[0])
   
   print(f"The chosen account {accno} has available balance £= {acc_balance}")
   
      
   cur.execute("SELECT * FROM account WHERE accno = ?",(accountno,))
   
   cur.execute("SELECT blimit FROM account WHERE accno =? ", (accountno,))
   
   blimit=float(cur.fetchone()[0])

   if acc_balance>=blimit: # Condition to check if account balance is greater than the limit ,
       
       acc_bal=float(acc_balance)-float(tamount)  #if condition met only then perform the transaction..
   
   flag=False
   
   while flag==False:
            
            taccountno=input("Enter the account number to which the funds have to be transferred to... ")
    
           
            if validate_value(taccountno)==True:
                
               if  account_no_validation(taccountno)==1:
       
                    taccountno=int(taccountno)

                    if (taccountno!=int(accountno)):

                        cur.execute("SELECT balance FROM account WHERE accno =? ", (taccountno,)) # query to fetch the balance of Account B
   

                        tacc_balance=float(cur.fetchone()[0])

                        flag=True

                    else:
                        print(f" Please enter the correct account number ( needs to be different from the current account numberi.e. {accountno} )")
                        flag=False

   

                    cur.execute("SELECT blimit FROM account WHERE accno =? ", (accountno,))
   

                    tblimit=float(cur.fetchone()[0])
                    
   
   tacc_bal=float(tacc_balance)+float(tamount)

   
   try:

       cur.execute(" SELECT * FROM account WHERE accno = ? ; ",(taccountno,))

   except TypeError:

       print("This is an incorrect value.")
       
   cur.execute("UPDATE account set balance = ? , ttime=CURRENT_TIMESTAMP  where accno = ? ",(acc_bal,accountno,))
   
   cur.execute("UPDATE account set balance = ? where accno = ? ",(tacc_bal,taccountno,))
   
        

   now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Updating the acc_transaction table with transaction details of account A ..
    
   cur.execute("INSERT into  acc_transaction (accno,balance,blimit,t_account,b_transaction,account_status,ttime) values(?,?,?,?,?,?,?)" ,(accno,acc_bal,blimit,taccountno,'Transfer Funds','ACTIVE',now))

   now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Updating the acc_transaction table with transaction details of account B..
    
   cur.execute("INSERT into  acc_transaction (accno,balance,blimit,t_account,b_transaction,account_status,ttime) values(?,?,?,?,?,?,?)" ,(taccountno,tacc_bal,tblimit,taccountno,'Transfer Funds','ACTIVE',now))
    
       
   transaction_history(accno)

   transaction_history(taccountno)

   flag=True

   con.commit()

      

def deposit_funds(accountno):

 
    damount=input("Please enter the amount to be deposited £ :") # Amount to be deposited


    

    acc_balance=0

    flag=False
    
    while flag==False:
        
             if validate_value(damount)==True:

                flag=True
                accno=int(accountno) 

    
     
       
    cur.execute("SELECT balance FROM account WHERE accno =? ", (accountno,))
   
    acc_balance=float(cur.fetchone()[0])

    print(f"The chosen account {accno} has available Balance £= {acc_balance}")

    cur.execute("SELECT blimit FROM account WHERE accno =? ", (accountno,))

    b_limit=float(cur.fetchone()[0])

    
    acc_bal=float(acc_balance)+float(damount) # add the deposit amount to the balance 
    
    taccount="Deposit Funds"

    cur.execute("UPDATE account set balance = ? where accno = ? ",(acc_bal,accountno,))
    
       
  
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cur.execute("INSERT into  acc_transaction (accno,balance,blimit,t_account,b_transaction,account_status,ttime) values(?,?,?,?,?,?,?)" ,(accno,acc_bal,b_limit,accno,'Deposit Funds','ACTIVE',now))
    
    transaction_history(accno)
    
    con.commit()

   

def account_info(lname,lpassword):
    
    cur.execute(" SELECT * FROM userlogindetails WHERE username = ? AND password = ? ", (lname, lpassword))

    rows = cur.fetchall()

    
    
    if len(rows) > 0:
        print("LOGIN SUCCESSFUL...")
        return 1 
    else:
        print("LOGIN UNSUCCESSFULL.. TRY AGAIN..")
        return 0
 

    

def transaction_history(accountno):
    
    print(f"\n TRANSACTIONS DETAILS  [ACCOUNT NO : {accountno} ]")
    
    cur.execute("SELECT accno,balance,b_transaction,ttime FROM acc_transaction   WHERE accno =? ORDER BY ttime", (accountno,))

    rows = cur.fetchall() 

    for row in rows:

        print(row)

def account_no_validation(accountno):
    
    while True:
        
        cur.execute(" SELECT accno from account WHERE accno = ? ",(accountno,))

        row=cur.fetchall()
    
        if len(row)>0:
            return 1
        else:
            return 0


def validate_value(check_num_value):
    
     
    SpecialSym =   ["$", "£","@","#", "%" ,"+","-", "&", "||", "!", "(", ")", "{", "}", "[", "]", "^","~", "*", "?","\"","\\",";",":","'",'"',"/",'>','<',',', '¬',"=","_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    validInt = True

    flag=0

    check_num_value=check_num_value.lower() # only lowercase alphabets will be parsed for data validation
    
    regexp = re.compile('[0-9a-zA-Z]+')

    if regexp.search(check_num_value):
       

        validInt=False
    

    if(check_num_value.isalpha()==True):
        
        validInt = False
                  
                 
        print('\n Incorrect value entered .. (alphabet values)')

           


    if (check_num_value.isdigit()==True):
        
        #print('\n Value entered is correct...')

         validInt = True
         flag=1
        
        
    if (check_num_value.isspace()==True):

     
        validInt = False

    if(check_num_value==""):

        validInt = False
          

        print('\n Incorrect value entered .. no value entered.')
  
        
       

    if(check_num_value in SpecialSym):
        
        print('\n Incorrect value... Use of special symbols or alphabets $ @ #-[ ] } { a -z ')
 

        validInt = False

        
    
  

    if(check_num_value.isnumeric()==True):

            # my_number=float(my_number) 

        validInt = True
        flag=1
    

   

               
    return validInt;


    
       
def main():

      while True:

       print(" \n=============================================================================")
       print("                                                                    BANK INTERFACE                                                                 ")
       print(" \n ==============================================================================")

       loginname=input("Enter the user name :")
      

       lpassword=input("Enter the password  :")
      

       if (account_info(loginname,lpassword)==1):
               

           cur.execute("SELECT accno FROM userlogindetails WHERE username = ? AND password = ? ", (loginname,lpassword))
        
           accountno=int(cur.fetchone()[0])
                  
           user_option_menu(accountno)

        
            
       
main()
