# import file handeling packages
import json
from pathlib import Path

path = Path("tasks.json")
task_list = []

# file exists check
if not path.exists():
    with open(path, 'w') as f:
        json.dump(task_list,f)

# load tasks file
def load_files():
    with open(path,'r') as f:
        tasks = json.load(f)
    return tasks

# save tasks 
def save_files(tasks):
    with open(path,'w') as f:
        json.dump(tasks,f,indent=2)

# main menu
menu = """Task List - Main Menu:
1.) Add, Update, or Delete tasks
2.) Marks as in progress or done
3.) List all tasks
4.) List all tasks that are done
5.) List all tasks that are not done
6.) List all tasks that are in progress
7.) Close program"""

def listTasks():
    tasks = load_files()
    for task in tasks:
        print(task)


def addTask():
    description = input("Enter a description of the task: ")
    tasks = load_files()
    id = len(tasks) + 1
    tasks.append({"ID":id,"Description":description,"Status":"to do"})
    save_files(tasks)

def updateTask():
    listTasks()
    index = int(input("Enter the ID of the task that you want to update: "))
    item = int(input("Enter (1) if you want to update the description or (2) if you want to update the status: "))
    tasks = load_files()
    if item == 1:
        new_description = input("Eneter the new description: ")
        tasks[index-1]["Description"] = new_description
        save_files(tasks)
    elif item == 2:
        new_status = input("Enter the new status: ")
        tasks[index-1]["Status"] = new_status
        save_files(tasks)

def deleteTask():
    r_id = int(input("Enter the ID of the task that you want to delete: "))
    tasks = load_files()
    del tasks[r_id - 1]
    save_files(tasks)

while True:
    print(menu)
    option = int(input("Select an option (1 - 7): "))
    if option == 1:
        choice = int(input("Enter (1) to add a new task, (2) to update an existing task, or (3) to delete a task: "))
        if choice == 1:
            addTask()
        elif choice == 2:
            updateTask()
        elif choice ==3:
            deleteTask()
    elif option == 2:
        new_status = int(input("""Enter (1) if the task is "in progress" or (2) if the task is "done": """))
        index = int(input("Enter the ID of task: "))
        tasks = load_files()
        if new_status == 1:
            tasks[index-1]["Status"] = "in progress"
        elif new_status == 2:
            tasks[index-1]["Status"] = "done"
        save_files(tasks)
    elif option == 3:
        listTasks()
    elif option == 4:
        tasks = load_files()
        for task in tasks:
            if task["Status"] == "done":
                print(task)
    elif option == 5:
        tasks = load_files()
        for task in tasks:
            if task["Status"] != "done":
                print(task)
    elif option == 6:
        tasks = load_files()
        for task in tasks:
            if task["Status"] == "in progress":
                print(task)
    elif option == 7:
        print("Exiting program")
        break
