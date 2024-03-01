# CAPSTONE PROJECT - finance_calculators.py : This program is to calculate interest on an investment or calculate the amount
# that should be repaid on a home loan each month..
#Create a program that allows the user to access two different financial calculators:
#an investment calculator and a homeloan calculator.
#investment : to calculate the amount of interest you'll earn on your investment.
#bond : to calculate the amount you'll have to pay on a home loan..

import math

print("\n CAPSTONE PROJECT -FINANCE CALCULATOR : An Investment Calculator and a Home Loan Calculator")
print("_____________________________________________________________________________")


"""Function verify_choice() To verify the choice of finance calculation - investment or bond """
        
def verify_choice():
    
      
    for i in range(5): # five turns to enter the correct choice...
        

        cal_choice=input("\n Please Enter Choice - Investment or Bond :")

        calculator_choice=cal_choice.lower()# converts the user entered value in lower case..

        if calculator_choice in ["Investment","investment","INVESTMENT","BOND","bond","Bond"]:

            return(calculator_choice)

        else:

            print("\n The choice you have entered is incorrect..Please enter correct Choice  :")


   


calculator_choice=str(verify_choice())
      

    
   
if(calculator_choice=="investment"):
  

    #user enters the amount of money that they are depositing.

            principal_amount=float(input("\n Please enter the amount of money that they are depositing :"))

    #enter the interest rate should be entered..

            interest_rate=float(input("\n Enter the interest rate % "))

    #number of years that they plan on investing..

            number_of_years=int(input("\n Enter the years they plan on investing.."))

    #please enter choice of Interest..

            choice_interest=int(input("\n Please enter choice of Interest 1. Simple 2.Compound "))

            if choice_interest==1:
    
            #simple interest on total amount..
    
                simple_interest_on_total_amount=principal_amount*(1+(interest_rate/100)
                                             *float(number_of_years))

                print("\n **************** SIMPLE INTEREST *******************")

                print(f"\n The simple interest on entered amount £ {simple_interest_on_total_amount}")

                print("\n ****************************************************")
            # compound interest on total amount..

            else:
                #compound interest formula
                
                compound_interest_on_total_amount=round((principal_amount*
                                      math.pow((1+interest_rate/100),
                                      float(number_of_years))),2)
    
                print("\n **************** COMPOUND INTEREST *******************")

                print(f"\n The compound interest on entered amount £ {compound_interest_on_total_amount}")

                print("\n ******************************************************")
    


# Bond



if(calculator_choice=="bond"):

        #present value of the house ...

            property_value=float(input("\n Present value of the house : "))
        
        #interest rate
        
            user_interest_rate=float(input("\n Enter the interest rate % "))

            bond_interest_rate=float(user_interest_rate/100)/12

       
            bond_number_of_months=int(input("\n Enter the number of months would you like to repay the bond.."))


            print("\n ****************HOME LOAN*******************")

            #Repayment formula
            
            repayment_amount=round(float((bond_interest_rate*property_value)
                             /(1-(1+bond_interest_rate)**(-bond_number_of_months)
                               )),2)
                             

            print(f"\n The monthly repayment for the Bond will be : {repayment_amount}")

            print("\n ***********************************************")

   
