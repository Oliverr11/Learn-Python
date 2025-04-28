import os
libraries = { 
    'Programming': [
        {'bookId': '10', 'bookName': 'C++', 'isBorrowed': False},
        {'bookId': '11', 'bookName': 'Python', 'isBorrowed': True},
        {'bookId': '12', 'bookName': 'The Journey', 'isBorrowed': True}
    ],
    'Math': [
        {'bookId': '14', 'bookName': 'Math For 1st Grade', 'isBorrowed': False},
        {'bookId': '18', 'bookName': 'The Journey', 'isBorrowed': True} 
    ],
    'Khmer':[
        {'bookId': '10', 'bookName': 'Khmer Book For 1st Grade', 'isBorrowed': False},
    ]
}
def addBook():
    print("==>> Add Book")
    displayCategory()
    category = input("Enter Category Name : ")
    searchCate = searchCategory(category)
    if searchCate != None : 
        bookId = input("Enter Book Id : ")
        for book in searchCate :
            if book['bookId'] == bookId:
                print("This Book  Id Already Exist!")
                return
        bookName = input("Enter Book Name : ")
       
        isBorrowed = False
        searchCate.append({
            "bookId": bookId,
            "bookName": bookName,
            "isBorrowed": isBorrowed
        })  
    else : 
        print("Category Not Found!")
def addCategory():
    print("=========== Add Category ===========")

    categoryName = input("Enter Category Name : ")
    searchCate = searchCategory(categoryName)
    if searchCate == None :
        libraries[categoryName] = []
        print(f"Category {categoryName} Add Successfully!")
        return
    print("This Category Already Exist!")

def searchCategory(categoryName):
    for key,value in libraries.items():
        if key.lower() == categoryName.lower():
            return value        
    return None
def searchBook(categoryName,bookName):
    searchCate = searchCategory(categoryName)
    if searchCate != None:
        for book in searchCate:
            if book['bookName'].lower() == bookName.lower():
                return book
    return None
def searchBooks(bookName): 
    print(f"==>> Book Name : {bookName} ")
    for keys,values in libraries.items():
        for value in values:
            if bookName.lower() == value['bookName'].lower() :
                print(f"Category : {keys} \n ID : {value['bookId']} \n Book Name : {value['bookName']} \n Borrow : {'Availible' if value['isBorrowed'] == False else 'Not Availible' }")
    
def menuSearchBook():
    print("=========== Search Book ===========")
    bookName = input("Enter Book Name : ")
    searchBooks(bookName)

    
def displayCategory():
    print("============== Categories ==============")
    index = 0
    for key,value in libraries.items():
        index+=1
        print(f"{index} : {key}")

def displayBook():
    print("========= Display Books =========")
    print("1) Display All Books")
    print("2) Display By Category")
    option = int(input("Enter Option (1-2) : "))
    match option :
        case 1:
            os.system('cls')
            displayAllBooks()
        case 2:
            os.system('cls')
            category = input("Enter Category Name : ")
            displayBooksByCategory(category)
        case _:
            print("Invalid Option!")

def returnOrBorrowBook(checkRB):
    print("==>> Return Book")
    displayCategory()
    categoryName = input("Enter Category : ")
    searchCate = searchCategory(categoryName)
    if searchCate != None:
        displayBooksByCategory(categoryName)
        bookName = input("Enter Book Name : ")
        sBook = searchBook(categoryName,bookName)
        if sBook != None : 
            if checkRB=='return':
                if  sBook['isBorrowed'] == True: 
                    sBook['isBorrowed'] = False
                    print("Return Successfully!")
                    return
                else:
                    print(f"{sBook['bookName']} Is Availible!")
                    return
            if checkRB=='borrow':
                if sBook['isBorrowed'] == False: 
                    sBook['isBorrowed'] = True
                    print("Borrow Successfully!")
                    return
                else:
                    print(f"{sBook['bookName']} Is Unavailible!")
                    return
        else:
            print("Book Not Found!")
            return
    print("Category Not Found!")
    
def displayAllBooks():
    print("=============== All Books ===============")
    for key,values in libraries.items():
        print(f"=> {key} : ")
        for value in values:
            print(f"  {value['bookId']}.{value['bookName']} [ {'Availible' if value['isBorrowed'] == False else 'Not Availible'} ]")

def displayBooksByCategory(categoryName):
    index = 0
    searchCate = searchCategory(categoryName)
    if searchCate != None :
         print(f"========= [{categoryName}] Books =========")
         for value in searchCate:
             index+=1
             print(f"{index}.{value['bookName']} [ {'Availible' if value['isBorrowed'] == False else 'Not Availible'} ]")
         return
    else : print("Category Not Found!")
    
def menu():
    os.system('cls')
    while True:
        print("===Library Management System ===")
        print("1) Add Book")
        print("2) Add Category")
        print("3) Borrow Book")
        print("4) Return Book")
        print("5) Display Books")
        print("6) Search Book")
        #print("10) Print List [Test]")
        print("7) Exit")
        try:
            option = int(input("Enter Option (1-7) : "))
        except ValueError:
            os.system('cls')
            print("Invalid input! Please enter a number.")
            continue 
        match option:
            case 1:    
                os.system('cls')
                #os.system('clear') #mac
                addBook()
            case 2:
                os.system('cls')
                #os.system('clear') #mac
                addCategory()
            case 3:
                os.system('cls')
                #os.system('clear') #mac
                returnOrBorrowBook("borrow")
            case 4:
                os.system('cls')
                #os.system('clear') #mac
                returnOrBorrowBook("return")
            case 5:
                os.system('cls')
                #os.system('clear') #mac
                displayBook()
            case 6:
                os.system('cls')
                #os.system('clear') #mac
                menuSearchBook()
            #case 10:
                #print(libraries)
            case 7:
                print("-"*50)
                print("Thank you for using the Library Management System!")
                print("-"*50)
                
                break
            case _:
                print("Invalid Choice!")
menu()