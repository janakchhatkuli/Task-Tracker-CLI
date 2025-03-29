import os 
import json
import argparse
import time

task_file = "task-tracker.json"

def load_task():
    if os.path.exists(task_file):
        with open(task_file,"r") as file:
            return json.load(file)
    return []
    
def save_task(tasks):
    with open(task_file,"w") as file:
        #print("file saved successfully")
        json.dump(tasks,file, indent=5)

def delete_task(task_id):
    tasks=load_task()
    tasks = [task for task in tasks if task["id"]!=task_id]
    save_task(tasks)
    print("Task deleted!")

def add_task(title):
 tasks=load_task()
 new_task ={
        "id":len(tasks)+1,
        "title" : title,
        #"description" :description,
        "status" : "incomplete",
        "add_time": time.ctime(time.time())
	}
 tasks.append(new_task)
 save_task(tasks)

def update_task():
     return
    
def main():
    parser = argparse.ArgumentParser(description="Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help ="Add a New Task")
    parser_add.add_argument("title",type=str,help="Task title")

    parser_add = subparsers.add_parser("delete", help ="Delete a Task")
    parser_add.add_argument("task_id",type=int,help="Task title")

    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title)
    if args.command == "delete":
        delete_task(args.task_id)
 

if __name__ == "__main__":
    main()