import os 
import json

task_file = "task-tracker.json"

def load_file():
    if os.path.exists(task_file):
        with open(task_file,"r") as file:
            return json.load(file)

def save_fie(tasks):
    with open(task_file,"w") as file:
        json.dumps(tasks,file, indent=5)

def delete_task():
     print("jkhfsj")
     return

def add_task(task):
	tasks=load_task()
	new_task ={
        "id":len(tasks)+1,
        "title" : title,
        "description" :description,
        "status" : 'incomplete'
	}
    

def update_task():
     return
    


 

