import os 
import json
import argparse
import time
from tabulate import tabulate

task_file = "task-tracker.json"
#function to load tasks from json file
def load_task():
    if os.path.exists(task_file):
        with open(task_file,"r") as file:
            return json.load(file)
    return []
#function to save task into json file    
def save_task(tasks):
    with open(task_file,"w") as file:
        #print("file saved successfully")
        json.dump(tasks,file, indent=5)
#function to delete the task 
def delete_task(task_id):
    tasks=load_task()
    tasks = [task for task in tasks if task["id"]!=task_id]
    save_task(tasks)
    print(f"Task deleted! :{task_id}")
#function to add new task 
def add_task(title):
 tasks=load_task()
 new_task ={
        "id":len(tasks)+1,
        "title" : title,
        "status" : "to-do",
        "add_time": time.ctime(time.time())
	}
 print(f"Task added :{new_task["title"]}")
 tasks.append(new_task)
 save_task(tasks)

#function to update the existing task
def update_task(task_id,new_title):
    tasks=load_task()
    for task in tasks :
        if task["id"] == task_id:
            task["title"] = new_title
            task["updated_time"] = time.ctime(time.time())
            print(f"Task updated :{task["title"]}")

    save_task(tasks)

#function to mark a task in progress
def mark_in_progress(task_id):
    tasks=load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["started_time"] = time.ctime(time.time())
            print(f"Task In Progress :{task["title"]}")
    save_task(tasks)

#function to mark a task done 
def mark_done(task_id):
    tasks=load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["completed_time"] = time.ctime(time.time())
            print(f"Task completed :{task["title"]}")
    save_task(tasks)
    






# Function to display tasks in a table format
def display_tasks(status=None):
    tasks = load_task()
    if status == "to-do":
        tasks = [task for task in tasks if task.get("status") == status]
    if status == "in-progress":
        tasks = [task for task in tasks if task.get("status") == status]
    if status == "done":
        tasks = [task for task in tasks if task.get("status") == status]


    # Convert tasks into a list of lists for tabulate
    table_data = []
    for task in tasks:
        table_data.append([
            task.get("id", "N/A"),
            task.get("title", "N/A"),
            task.get("add_time", "N/A"),
            task.get("updated_time", "N/A"),
            task.get("status","N/A"),
            task.get("started_time","N/A"),
            task.get("completed_time","N/A")
        ])

    # Define column headers
    headers = ["Task ID", "Title", "Created Time", "Updated Time","Status","Started Time","Completed Time"]

    # Print the table
    

    print(tabulate(table_data, headers=headers, tablefmt="grid"))






def main():
    parser = argparse.ArgumentParser(description="Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add", help ="Add a New Task")
    parser_add.add_argument("title",type=str,help="Task title")

    parser_add = subparsers.add_parser("delete", help ="Delete a Task")
    parser_add.add_argument("task_id",type=int,help="Task ID")

    parser_add = subparsers.add_parser("update", help ="Update a Task")
    parser_add.add_argument("task_id",type=int,help="Task ID")
    parser_add.add_argument("title",type=str,help="Task title")

    parser_add = subparsers.add_parser("mark-in-progress", help ="Mark a Task in Progress")
    parser_add.add_argument("task_id",type=int,help="Task ID")

    parser_add = subparsers.add_parser("mark-done", help ="Mark a Task Done")
    parser_add.add_argument("task_id",type=int,help="Task ID")

    parser_add = subparsers.add_parser("list-tasks", help ="List The Tasks")
    parser_add.add_argument("status",type=str,help="Status of Task")

    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.title)
    if args.command == "delete":
        delete_task(args.task_id)
    if args.command == "update":
        update_task(args.task_id,args.title)
    if args.command == "mark-done":
        mark_done(args.task_id)
    if args.command == "list-tasks":
        display_tasks(args.status)
 

if __name__ == "__main__":
    main()