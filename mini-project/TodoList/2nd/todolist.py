import json
from datetime import datetime
class TodoList():
    pass 
    
    def __init__(self,description=""):
        self.tasks=[]
        self.description = description
        self.completed = False
        self.loadFile() 
    def addTask(self,description):
        task = {
            'id':len(self.tasks)+1,
            'description': description,
            'completed':False,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.saveFile()
    def viewTasks(self):
        for task in self.tasks:
            print(f"{task['id']}. [ {'❌' if task['completed']==False else '✅'} ] {task['description']}")
    
    def completeTask(self,id):
        for task in self.tasks:
            if id == task['id']:
                task['completed'] = True
                self.saveFile()
                return 
        print("Task Not Founded!")
        
    def deleteTask(self,id):
        for task in self.tasks:
            if id == task['id']:
                self.tasks.remove(task)
                print(f"Delete task {id} successfully!")
                self.saveFile()
                return
        print("Task Not Found!")
    
    def saveFile(self):
        with open('2ndTasks.json','w') as file:
            json.dump(self.tasks,file,indent=4)
    def loadFile(self):
        try:
            with open('2ndTasks.json','r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("File Not Found!")
todoList = TodoList()
def addTask():
    description = input("Enter Description : ")
    todoList.addTask(description)
def viewTasks():
    todoList.viewTasks()
def completeTask():
    viewTasks()
    id = int(input("Enter Id : "))
    todoList.completeTask(id)
def deleteTask():
    viewTasks()
    id = int(input("Enter Id : "))
    todoList.deleteTask(id)
def menu():
    
    while True:
        print("-"*20)
        print("1. Add Task ")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("Enter Choice (1-5) "))
        match choice :
            case 1 : 
                addTask()
            case 2 :
                viewTasks()
            case 3 :
                completeTask()
            case 4 : 
                deleteTask()
            case 5 :
                break
            case _:
                print("Invalid Choice!")
                
menu()
