bankAccounts =[]
def create_account():
    account_number = int(input("Enter Account Number : "))
    account_holder = input("Enter Account Holder : ")  
    balance = float(input("Enter Balance : "))
    bacnkAccount = (account_number,account_holder,balance)
    bankAccounts.append(bacnkAccount)
    print(" ✅ Add Successfully!")
    
def display_accounts():
    print("======Accounts======")
    for bankAccount in bankAccounts:
        account_number,account_holder,balance = bankAccount
        print(f"Account Number : {account_number}, Account Holder : {account_holder}, Balance : {balance}")

def deposit_money():
    display_accounts()
    accNumber = int(input("Enter Account Number : "))
    account = search_account(accNumber)
    if account != None:
        for index, bankAccount in enumerate(bankAccounts):
            account_number,_,balance=bankAccount
            if account_number == accNumber:
                depoBalance = float(input("Enter Balance : "))
                balance += depoBalance
                bankAccountBalance = (account_number,_,balance)
                bankAccounts[index]=bankAccountBalance
                print(" ✅ Deposit Successfully!")
                return
    print("Account Not Found!")
            
def withdraw_money():
    display_accounts()
    accNumber = int(input("Enter Account Number : "))
    account = search_account(accNumber)
    if account != None:
        for index, bankAccount in enumerate(bankAccounts):
            account_number,_,balance=bankAccount
            if account_number == accNumber:
                withdrawBalance = float(input("Enter Balance : "))
                if withdrawBalance < balance :
                    balance -= withdrawBalance
                    bankAccountBalance = (account_number,_,balance)
                    bankAccounts[index] = bankAccountBalance
                    print(" ✅ Withdraw Successfully!")
                    return
    print("Invalid Account Or Balance Not Enoguht!!")

def remove_account():
    display_accounts()
    accNumber = int(input("Enter Account Number : "))
    account = search_account(accNumber)
    if account != None:
        bankAccounts.remove(account)
        print(" ✅ Remove Successfully!")
        return
    print("Account Not Found!")
    
def search_account(accountNumber):
    for bankAccount in bankAccounts:
        account_number,*_ = bankAccount
        if account_number == accountNumber :
            return bankAccount
    return None

def menu():
    while(True) : 
        print("==========STEP BANK==========")
        print("1. Create Account")
        print("2. Display Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Remove Account")
        choice = int(input("Enter Choice : "))
        match choice : 
            case 1:
                create_account()
            case 2:
                display_accounts()
            case 3:
                deposit_money()
            case 4:
                withdraw_money()
            case 5:
                remove_account()
            case _:
                return
        
menu()