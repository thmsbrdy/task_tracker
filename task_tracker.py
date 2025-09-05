menu = """Task List - Main Menu:
1.) Add, Update, or Delete tasks
2.) Marks as in progress or done
3.) List all tasks
4.) List all tasks that are done
5.) List all tasks that are not done
6.) List all tasks that are in progress
7.) Close program"""

class Task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status

    def toString(self):
        return self.id, self.description, self.status

taskList = []

def listTasks():
    for task in taskList:
        print(task.toString())

def addTask():
    description = input("Enter a description of the task: ")
    id = len(taskList) + 1
    status = "to do"
    newTask = Task(id, description, status)
    taskList.append(newTask)
    print(newTask.toString())

def updateTask():
    listTasks()
    index = int(input("Enter the ID of the task that you would like to update: "))
    choice = int(input("Enter (1) to update the description or (2) to update the status: "))
    if choice == 1:
        taskList[index-1].description = input("Enter the new description: ")
    if choice == 2:
        taskList[index-1].status = input("Enter the new status: ")

while True:
    print(menu)
    option = int(input("Select an option (1 - 4): "))
    if option == 1:
        choice = int(input("Enter (1) to add a new task, (2) to update an existing task, or (3) to delete a task: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            updateTask()
    elif option == 2:
        print("wip")
    elif option == 3:
        listTasks()
    elif option == 4:
        print("wip")
    elif option == 5:
        print("wip")
    elif option == 6:
        print("wip")
    elif option == 7:
        print("Exiting program")
        break




