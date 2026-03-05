import random
import os

print("Welcome to GAR's Bank 😃")
print("Want to create a bank account?")
print("enter 1 for creating an account ")
print("enter 2 for checking account details ")
print("enter 3 for depositing money")
print("enter 4 for withdrawing money")
user_input = int(input())

class Bank_Acc:
    def __init__(self,name,age,Aadhaar_No,Account_No,user_balance=0):
        self.name = name
        self.age = age
        self.Aadhaar_No = Aadhaar_No
        self.Account_No = Account_No
        self.user_balance = user_balance

    def save_user_data(self):
        with open(f"{self.name}.txt", "a") as file:
            file.write(f"user name : {self.name}\n")
            file.write(f"user age : {self.age}\n")
            file.write(f"user Adhaar : {self.Aadhaar_No}\n")
            file.write(f"user Account : {self.Account_No}\n")
            file.write(f"user balance : {self.user_balance}\n")



if user_input == 1:
    user_name = input("enter your name : ")
    user_age= int(input("enter your age : "))
    if user_age < 18:
        print("Sorry! Account cant be created for below 18")
        exit()

    user_Aadhaar = int(input("enter the aadhaar no."))

    if type(user_Aadhaar) ==  int and len(user_Aadhaar) != 12:
        print("please enter correct aadhaar no.")
        exit

    print("Congrats 👍 your account is created ")
    user_Account = random.randint(1000,10000)
    print(f"your account no. is {user_Account}")

    obj = Bank_Acc(user_name,user_age,user_Aadhaar,user_Account,user_balance=0)
    obj.save_user_data()
    

elif user_input == 2:

    user_name = input("please enter your name")
    if os.path.exists(f"{user_name}.txt"):
        print("Here are your account details")

        with open(f"{user_name}.txt", "r") as f:
            for line in f:
                print(line.strip())  # strip() removes \n
    else:
        print("Sorry not valid account holder")

elif user_input == 3:

    user_name = input("please enter your name")
    if os.path.exists(f"{user_name}.txt"):
        amount = int(input("enter the amount to be deposited"))
        
        with open(f"{user_name}.txt", 'r') as f:
            lines = f.readlines()

            balance = int(lines[4].split(":")[1])  

        new_amount = balance + amount

        lines[4] = f"user balance : {new_amount}\n"

        with open(f"{user_name}.txt", "w") as f:
            f.writelines(lines)

        print(f"Money deposited! your current balance is : {new_amount}")

elif user_input == 4:

    user_name = input("please enter your name ")
    if os.path.exists(f"{user_name}.txt"):
        amount = int(input("enter the amount to be deposited"))
        
        with open(f"{user_name}.txt", 'r') as f:
            lines = f.readlines()

            balance = int(lines[4].split(":")[1])  

        new_amount = balance - amount

        lines[4] = f"user balance : {new_amount}\n"

        with open(f"{user_name}.txt", "w") as f:
            f.writelines(lines)

        print(f"Money withdrawn! your current balance is : {new_amount}")


        
        