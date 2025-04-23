students=[]
# def add_student():
#     id = int(input("Enter ID : "))
#     name = input("Enter Name : ")
#     age = int(input("Enter Age : "))
#     dupId = search_student(id)
#     if dupId == None:
#         student = (id,name,age)
#         students.append(student)
#         print("Add Successfully!")
#     print("User ID Exist!")
    


def add_student():
    
    id = len(students) +1
    print(f"Id : {id}")
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    student = (id,name,age)
    students.append(student)
    print("Add Successfully!")
    
    
    
def display_student():
    print("======Students======")
    for student in students:
        id,name,age=student
        print(f"ID : {id}, Name : {name}, Age : {age}")
    print("====================")
    
def remove_student():
    student_id = int(input("Enter Student Id To Delete : "))
    student = search_student(student_id)
    if student != None :
        students.remove(student)
        return
    print("No Student Found!")
    
def search_student(studentId):
    for student in students:
        id,*other = student
        if id == studentId:
            return student
    return None

def update_student():
    student_id = int(input("Enter Student Id To Delete : "))
    student = search_student(student_id)
    if student != None :   
        for index, student in enumerate(students):
            id,*other = student
            if id == student_id:
                newName = input("Enter Name : ")
                newAge = input("Enter Age : ")
                update_student = (student_id,newName,newAge)
                students[index] = update_student
                print("Update Successfully!")
                return
    print("Student Not Founded!")
    

def menu ():
    while True:
        print("====================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")  
        print("4. Update Student") 
        print("5. Exit")
        option = int(input("Enter Opt : "))
        match option:
            case 1:
                add_student()
            case 2:
                remove_student()
            case 3:
                display_student()
            case 4:
                update_student()
            case 5:
                return
            case _:
                print("Invalid choice.")
        
    
menu()
        

