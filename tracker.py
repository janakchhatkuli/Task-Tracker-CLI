import os 
import json
import argparse

task_file = "task-tracker.json"

def load_task():
    if os.path.exists(task_file):
        with open(task_file,"r") as file:
            return json.load(file)
    return []    
def save_task(tasks):
    with open(task_file,"w") as file:
        json.dumps(tasks,file, indent=5)

def delete_task(task_id):
     tasks=load_tasks()
     tasks = [task for task in tasks if task["id"]!=task_id]
     save_task(tasks)
     print("Task deleted!")

def add_task(title,description):
	tasks=load_task()
	new_task ={
        "id":len(tasks)+1,
        "title" : title,
        "description" :description,
        "status" : "incomplete"
	}
    tasks.append(new_task)
    save_task(tasks)

def add_task(title, description):
    tasks = load_task()  # ✅ Fixed indentation
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "incomplete"
    }
    tasks.append(new_task)  # ✅ Fixed indentation
    save_task(tasks)        # ✅ Fixed indentation


def update_task():
     return
    
def main():
     parser = argparse.ArgumentParser(description="Task Tracker")
     subparsers = parser.add_subparsers(dest="command")

     parser_add = subparsers.add_parsers("add", help ="Add a New Task")
     parser_add.add_argumet("title",type=str,help="Task title")

    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title)

 

