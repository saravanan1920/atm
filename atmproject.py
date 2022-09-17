import time

#dose  the following basic ATM requirements:-

print("-------------------------------")
print("*******************************")
print("WELCOME TO BESANT ATM")
print("*******************************")
print("-------------------------------")
print("")
print("")

#ATM pin(password)statement:-

print("-------------------------------")
print("Please Insert your ATM Card")
print("-------------------------------")

time.sleep(3)

password = 1234

pin = int(input("Enter your atm pin:"))

balance = 5000

if pin == password:
    while True:

        print("""
        1--balance checking
        2--withdraw amount
        3--deposit amount
        4--mini statement
        5--exit
       """ )
       

        try:
            option = int(input("Please Enter your choise:"))
        except:
            print("--------------------------")
            print("Elease Enter valid optiion")
            print("--------------------------")

    #balance checking:-

        if option==1:
            print("--------------------------")
            print(f"your current balance is {balance}")
            print("--------------------------")

    #withdraw amount:-

        if option==2:
            withdraw_amount=float(input("please enter withdraw_amount:"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited your account")
            print(f"your updated balance is {balance}:")
            print("------------------------------------")
            print("THANK YOU FOR USING BESANT ATM")
            print("")
            print("your Amount is successfully Withdraw")
            print("-------------------------------------")

    #deposit amount:-
        
        if option==3:
            deposit_amount = float(input("Please Enter deposit_amount"))
            balance=balance+deposit_amount
            print(f"Your Updated balance is {balance}:")
            print("THANK YOU FOR USING BESANT ATM")
           
            print("Your Amount is Successfully Deposited in your Account")


        if option==4:
            print("--------------------------")
            print("--------------------------")
            print(f"current balance:{balance}")
            print("--------------------------")
            print("--------------------------")
          
    #exit statement:-
           
        if option==5:
            break
        
else:
    print("Invalied Pin , RETRY")



#***********************************************************************************************
    #OUTPUT:- 
#
#*******************************
#WELCOME TO BESANT ATM
#*******************************
#-------------------------------


#-------------------------------
#Please Insert your ATM Card
#-------------------------------
#Enter your atm pin:1234

 #       1--balance checking
  #      2--withdraw amount
   #     3--deposit amount
    #    4--mini statement
     #   5--exit

##--------------------------
#your current balance is 5000
#-------------------------

 #       1--balance checking
  #      2--withdraw amount
   #     3--deposit amount
    #    4--mini statement
     #   5--exit

#Please Enter your choise:2
#please enter withdraw_amount:2000
#2000.0 is debited your account
#your updated balance is 3000.0:
#------------------------------------
#THANK YOU FOR USING BESANT ATM

#your Amount is successfully Withdraw
#-------------------------------------

 #       1--balance checking
  #      2--withdraw amount
   #     3--deposit amount
    #    4--mini statement
     #   5--exit

#Please Enter your choise:3
#Please Enter deposit_amount2000
#Your Updated balance is 5000.0:
#THANK YOU FOR USING BESANT ATM
#Your Amount is Successfully Deposited in your Account

 #       1--balance checking
  #      2--withdraw amount
   #     3--deposit amount
    #    4--mini statement
     #   5--exit

#Please Enter your choise:4
#--------------------------
#--------------------------
#current balance:5000.0
#--------------------------
#--------------------------

 #       1--balance checking
  #      2--withdraw amount
   #     3--deposit amount
    #    4--mini statement
     #   5--exit

#Please Enter your choise:5
#PS C:\Users\ELCOT\Desktop\python pro\MySQL\covid19>""""
#********************************************************************************************************************