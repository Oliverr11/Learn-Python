accounts = {}
def createAccount():
    acc_number= int(input("Enter Account Number : "))
    acc_holder = input("Enter Account Holder : ")
    balance = float(input("Enter Balance : "))
    accounts[acc_number]={"holder" : acc_holder,"balance" : balance}
    print(accounts)
    print("Account Created Successfully!")

def displayAccount():
    for acc_number,info in accounts.items():
        print(f"Account Number : {acc_number}, Holder : {info['holder']}, Balance : {info['balance']}$")
    
def depositMoney():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        depositBalance = float(input("Enter Balance : "))
        searchingAcc["balance"] += depositBalance
        accounts[userAccNumber] = {"holder":searchingAcc["holder"],"balance":searchingAcc["balance"]}
    else :
        print("Account Not Founded!")

    
def withdrawMoney():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        withdrawMoney = float(input("Enter Balance : "))
        if withdrawMoney<searchingAcc["balance"]:
            searchingAcc["balance"] -= withdrawMoney
            accounts[userAccNumber] = {"holder":searchingAcc["holder"],"balance":searchingAcc["balance"]}
        else:
            print("You Don't Have Enought Balance!")    
    else :
        print("Account Not Founded!")
        
def searchByAccountNumber(number):
    for account,info in accounts.items():
        if number == account:
            return info
    return None
    
def removeByAccountNumber():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
    if searchingAcc is not None:
        del accounts[userAccNumber]
             
def searchAccount():
    userAccNumber = int(input("Enter Account Number : "))
    searchingAcc = searchByAccountNumber(userAccNumber)
   
    if searchingAcc is not None:
        holder = searchingAcc["holder"]
        balance = searchingAcc["balance"]
        print(f"Account Number : {userAccNumber}, Account Holder : {holder}, Balance : {balance}$")
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