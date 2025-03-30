# Task-Tracker-CLI
A CLI app to track your tasks and manage your to-do list.

link to project instructions https://roadmap.sh/projects/task-tracker

All The Commands Are Listed Below

# Adding a new task
python tracker.py add "Buy groceries"
# Task added successfully (ID: 1)

# Updating and deleting tasks
python tracker.py update 1 "Buy groceries and cook dinner"
python tracker.py delete 1

# Marking a task as in progress or done
python tracker.py mark-in-progress 1
python tracker.py mark-done 1

# Listing all tasks
python tracker.py list-tasks

# Listing tasks by status
python tracker.py list-tasks done
python tracker.py list-tasks to-do
python tracker.py list-tasks in-progress
