import json
tasks=[]
class Task:
    pass
    def __init__(self,title="Untitled",description="No Description"):
        self.title = title
        self.description = description
        self.isCompleted = False

def addTask():
    newTask = Task()
    print("===========Add Task=============")
    newTask.title = input("Title : ")
    newTask.description = input("Description : ")
    tasks.append(newTask)
    saveTasks()
    
def viewTasks():
    print("===========All Tasks============")
    for task in tasks:
        print(f"Task : {task.title}\n  Description : {task.description}\n  Complete : {'Done' if task.isCompleted else 'Not Done'}")

def markAsDone():
    viewTasks()
    titleSearch = input("Enter Task Title To Mark As Done : ")
    taskFound = searchTask(titleSearch)
    if taskFound != None:
        if taskFound.title == titleSearch:
            taskFound.isCompleted = True
            saveTasks()
            
    else:
        print("Task Not Founded!")
        
def deleteTask():
    viewTasks()
    titleSearch = input("Enter Task Title To Delete : ")
    taskFound = searchTask(titleSearch)
    if taskFound != None:
        if taskFound.title == titleSearch:
            tasks.remove(taskFound)
            saveTasks()
            

def editTask():
    viewTasks()
    titleSearch = input("Enter Task Title To Edit : ")
    taskFound = searchTask(titleSearch)
    if taskFound != None :
        if taskFound.title == titleSearch:
            newTitle = input("Enter New Title : ")
            newDescription = input("Enter New Description : ")
            taskFound.title = newTitle
            taskFound.description = newDescription
            saveTasks()

def searchTask(title):
    for task in tasks:
        if task.title == title:
            return task
    return None

def saveTasks():
    with open("tasks.json","w") as file:
        task_data = [{"title":task.title,"description":task.description,"isCompleted":task.isCompleted} for task in tasks]
        json.dump(task_data,file,indent=4)

def loadTasks():
        with open("tasks.json","r") as file:
            task_data = json.load(file)  
            tasks.clear()
            for task_dict in task_data:
                task = Task(task_dict["title"], task_dict["description"])
                task.isCompleted = task_dict["isCompleted"]  
                tasks.append(task)

def menu():
    loadTasks()
    while True:
        print("===========ToDo-List===========")
        print("1) Add a task")
        print("2) View tasks")
        print("3) Mask task as done")
        print("4) Delete a task")
        print("5) Edit a task")
        print("6) Exit")
        choice = int(input("Enter Task : "))
        match choice:
            case 1:
                addTask()
            case 2:
                viewTasks()
            case 3:
                markAsDone()
            case 4:
                deleteTask()
            case 5:
                editTask()
            case 6:
                break
            case _:
                print("Invalid Choice!")

menu()