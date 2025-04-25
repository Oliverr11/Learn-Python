accounts = []
def createAccount():
    acc_number= int(input("Enter Account Number : "))
    acc_holder = input("Enter Account Holder : ")
    balance = float(input("Enter Balance : "))
    account = (acc_number,acc_holder,balance)
    accounts.append(account)
    print("Account Created Successfully!")

def displayAccount():
    for account in accounts:
        acc_number,acc_holder,balance = account
        print(f"Account Number : {acc_number}, Holder : {acc_holder}, Balance : {balance}$")
    
def depositMoney():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        for index, account in enumerate(accounts):
            acc_number,acc_holder,balance = account
            if acc_number == userAccNumber :
                depositBalance = float(input("Enter Balance : "))
                balance += depositBalance
                accounts[index] = (acc_number,acc_holder,balance)
                print(accounts[index])
    else :
        print("Account Not Founded!")

    
def withdrawMoney():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        for index, account in enumerate(accounts):
            acc_number,acc_holder,balance = account
            if acc_number == userAccNumber :
                withdrawMoney = float(input("Enter Balance : "))
                if withdrawMoney<balance:
                    balance -= withdrawMoney
                    accounts[index] = (acc_number,acc_holder,balance)
                    print(accounts[index])
                else:
                    print("You Don't Have Enought Balance!")
    else :
        print("Account Not Founded!")
        
def searchByAccountNumber(number):
    for account in accounts:
        acc_number,*_=account
        if acc_number == number:
            return account
    return None


def searchByAccountNumber2(number):
    for account in accounts:
        acc_number,*_=account
        if acc_number == number:
            return account
    return None


    
def removeByAccountNumber():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        for index, account in enumerate(accounts):
            acc_number,acc_holder,balance = account
            if acc_number == userAccNumber:
                accounts.pop(index)
                
def searchAccount():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        acc_number,acc_holder,balance=searchingAcc
        print(f"Account Number : {acc_number}, Account Holder : {acc_holder}, Balance : {balance}$")
    else:
        print("Account Not Founded!")
        
def menu():
    while True :
        print("============MENU============")
        print("1) Create Account")
        print("2) Display All Accounts")
        print("3) Deposit Money")
        print("4) Withdraw Money")
        print("5) Remove Account")
        print("6) Search Account")
        choice= int(input("Enter Choice : "))
        match choice:
            case 1:
                createAccount()
            case 2:
                displayAccount()
            case 3:
                depositMoney()
            case 4:
                withdrawMoney()
            case 5:
                removeByAccountNumber()
            case 6:
                searchAccount()
            case _:
                print("Invalid Choice")

menu()