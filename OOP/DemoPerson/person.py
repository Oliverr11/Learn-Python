class Person:
    #constructor
    def __init__(self,id,name):
        self.id = id
        self.name = name
        
    #override string(str) method
    def __str__(self):
        return f"id : {self.id} name : {self.name}"
    
    def greet(self):
        print(f"Hello {self.name}")

