todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    
def show_all_tasks(tasks: list) -> None:
    if tasks:
        for i,v in enumerate(tasks, start=1):
            print(f'index: {i} mission: {v}')
    else:        
        print("the list is empty")
    
def get_user_choice() -> str:
    print('''  
                1. Adding a task 
                2. Show all tasks 
                3. Deleting a task
                4. Editing a task
                5. exit
                ''')
    
    user_input = input("choice a num from menu: ")
    return user_input

def delete_task(tasks: list, index: int) -> bool:
    del tasks[index]

def edit_task(tasks: list, index: int, new_task: str) -> bool:
        tasks[index] = new_task
        print("\n----the chenged complet----")

def get_task_index_from_user() -> int:
    user = int(input("enter a number of index: "))
    return user - 1
    

def main() -> None:
    while True:
        status_user = get_user_choice()
        if status_user == "1":
            user = input("enter a mission: ")
            add_task(todo_list, user)
        elif status_user == "2":
            show_all_tasks(todo_list)
        elif status_user == "3":
            user_del = get_task_index_from_user()
            if user_del in range(len(todo_list)):
                delete_task(todo_list, user_del)
            else:
                print("\n!!!wrong index!!!")
        elif status_user == "4":
            user_index = get_task_index_from_user()
            if user_index in range(len(todo_list)):
                user_change = input("enter a update mission: ")
                edit_task(todo_list, user_index, user_change)
            else:
                print("!!!wrong index!!!")
        elif status_user == "5":
             break  
      
main()
    
    