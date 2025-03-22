tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

# adding a remove task feature 
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()