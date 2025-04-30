from student import Student
students = []

def add_student():
    student = Student.default()
    student.input()
    students.append(student)
    
def display_student():
    for student in students:
        print(student)
        
def search_student():
    student_id = int(input("Enter Student Id : "))
    for student in students:
        if student_id == student.id:
            print(student)
            return
    return None

def remove_student():
    student_id = int(input("Enter Student Id : "))
    for student in students:
        if student_id == student.id:
            students.remove(student)
            print(f"Student Id : {student.id} has been removed!")
            return
    return None

def menu():
    while True:
        print("=========STEP=========")
        print("1) Add Student")
        print("2) Display Students")
        print("3) Search Student")
        print("4) Remove Student")
        option = int(input("Enter Option : "))
        match option:
            case 1 :
                add_student()
            case 2 : 
                display_student()
            case 3 : 
                search_student()
            case 4 : 
                remove_student()
            case _:
                print("Invalid Option!")

menu()


