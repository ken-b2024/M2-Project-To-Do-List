menu_items = ['1. Add a task',
            '2. View tasks', 
            '3. Mark a task as complete', 
            '4. Delete a task',
            '5. Quit'
]
task_list = [

]
def main_menu():
    print("Welcome to the To-Do List App!")
    print("\n")
    print('Menu:', *menu_items, sep='\n ')
def add_task():
            action = input("Enter task or exit to return to Main Menu: ")
            if action.lower() != 'exit':
                task_list.append(action + ' Incomplete')
                print("\nTask added!")
                multiple_task_add()
            elif action == 'exit':
                print("\nReturning to menu")
def view_task():
    if task_list:
        print('\n''Current Tasks:', *task_list, sep='\n -')
    else:
        print("\nNo tasks available.")
def change_task():
    global task_list
    if not task_list:
        print("\nNo tasks available. Returning to Main Menu.")
        return
    view_task()
    action = str(input("Enter task to complete or exit: "))
    if action == 'exit':
        print("\nReturning to main menu.")
    for i, task in enumerate(task_list):
        if task.startswith(action):
            task_list[i] = task.replace('Incomplete', 'Complete')
            print("\nTask marked as complete!")
            multiple_task_change()
            break
    else:
        print("\nNot a valid task. try again...")
        return
def remove_task():
    view_task()
    action = input("Enter task to remove or exit to return to Main Menu: ")
    if action == 'exit':
        print("\nReturning to menu")
        return
    for i, task in enumerate(task_list):
         if task.startswith(action):
            task_list.remove(task)
            print("\nTask removed!")
            multiple_task_remove()
            break
    else:
        print("\nNot a valid task. Try again...")
def multiple_task_add():
        while True:
            action = input("Add another task or exit: ")
            if action == 'exit':
                print("\nReturning to main menu.")
                break
            else:
                task_list.append(action + ' Incomplete')
                print("\nTask added!")
def multiple_task_change():
    while True:
        view_task()
        action = str(input("Enter next task to complete or exit for main menu: "))
        if action == 'exit':
            print("\nReturning to main menu.")
            break
        for i, task in enumerate(task_list):
            if task.startswith(action):
                task_list[i] = task.replace('Incomplete', 'Complete')
                print("\nTask marked as complete!")
                break
        else:
            print("\nTask not found. Try again...")
            break
def multiple_task_remove():
    while True:
        view_task()
        action = input("Remove another task or exit: ")
        if action == 'exit':
                print("\nReturning to main menu.")
                break
        for i, task in enumerate(task_list):
            if task.startswith(action):
                task_list.remove(task)
                print("\nTask removed!")
        else:
            print("\nNot a valid task. Try again...")
while True:
    main_menu()
    try:
        user_action = int(input("Please select a menu item number: ")) #must be an integer
        if user_action == 1:
            add_task()
        if user_action == 2:
            view_task()
        if user_action == 3:
            change_task()
        if user_action == 4:
            remove_task()
        if user_action == 5:
            print("\nThanks for trying the app! Goodbye!")
            break
    except ValueError:
        print("\n")
        print("That is not a valid selection. Try again...")