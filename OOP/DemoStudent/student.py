class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Id : {self.id}, Name : {self.name}, Age : {self.age}"
    
    @classmethod
    def default(cls):
        return Student(0,"",0)
    
    def input(self):
        self.id = int(input("Enter ID : "))
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))