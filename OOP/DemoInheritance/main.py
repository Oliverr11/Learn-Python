class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        
    def display(self):
        print(f"Id : {self.id}, Name : {self.name}")

    def eat(self):
        print(f"{self.name} is eating..." )

    def walk(self):
        print(f"{self.name} is walking...")
        
class Student(Person):
    def __init__(self, id, name,age,address):
        super().__init__(id, name)
        self.age = age
        self.address = address
    
    def display(self):
        super().display()
        print(f"Age : {self.age}, Address : {self.address} \n")
        print(f"Id : {self.id}, Name : {self.name}, Age : {self.age}, Address : {self.address}")
        
    def study(self):
        print(f"{self.name} is studying...")

    
        
person = Person(1,"Sengkim")
student = Student(1,"Taing Sengkim",18,"Phnom Penh")
        
student.eat()
student.walk()
student.study()
student.display()
        