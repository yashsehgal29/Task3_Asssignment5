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
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task index.")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a Task")
    print("2. List All Tasks")
    print("3. Remove a Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            print("Your Tasks =======>")
            list_tasks()
        elif choice == '3':
            list_tasks()
            if tasks:
                try:
                    task_index = int(input("Enter the task number to remove: "))
                    remove_task(task_index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Exited !")
            break
          
if __name__ == "__main__":
    main()