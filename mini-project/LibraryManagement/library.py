libraries = { 
    'Programming': [
        {'bookId': '10', 'bookName': 'C++', 'isBorrowed': False},
        {'bookId': '11', 'bookName': 'Python', 'isBorrowed': True}
    ],
    'Math': [
        {'bookId': '12', 'bookName': 'Math For 1st Grade', 'isBorrowed': False}
    ]
}
def addBook():
    displayCategory()
    category = input("Enter Category : ")
    searchCate = searchCategory(category)
    if searchCate != None : 
        bookName = input("Enter Book Name : ")
        bookId = input("Enter Book Id : ")
        isBorrowed = False
        libraries[category].append({
            "bookId": bookId,
            "bookName": bookName,
            "isBorrowed": isBorrowed
        })  
    else : 
        print("Category Not Found!")
def addCategory():
    category = input("Enter Category Name : ")
    libraries[category] = []

def searchCategory(categoryName):
    for key,value in libraries.items():
        if key == categoryName:
            return value        
    return None

def displayCategory():
    print("===Categories===")
    index = 0
    for key,value in libraries.items():
        index+=1
        print(f"{index} : {key}")

def displayBook():
    print("===Display Books===")
    print("1) Display All Books")
    print("2) Display By Category")
    option = int(input("Enter Option (1-2) : "))
    match option :
        case 1:
            displayAllBooks()
        case 2:
            category = input("Enter Category Name : ")
            displayBooksByCategory(category)
        case _:
            print("Invalid Option!")

def displayAllBooks():
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
    while True:
        print("===Library Management System ===")
        print("1) Add Book")
        print("2) Add Category")
        print("3) Borrow Book")
        print("4) Return Book")
        print("5) Display Books")
        print("6) Search Book")
        print("10) Print Lists")
        print("7) Exit")
        option = int(input("Enter Option (1-7) : "))
        match option:
            case 1:
                addBook()
            case 2:
                addCategory()
            case 5:
                displayBook()
            case 10:
                print(libraries)
            case _:
                print("Invalid Choice!")
                
menu()