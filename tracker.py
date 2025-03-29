import os 
import json

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
        "status" : 'incomplete'
	}
    tasks.append(new_task)
    save_task(tasks)


def update_task():
     return
    


 

