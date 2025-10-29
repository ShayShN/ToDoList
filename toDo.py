
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
                6. search for a word
                7. Mark as done
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
    
def search_tasks(tasks: list, keyword: str) -> list:
    arr = []
    for i,v in enumerate(tasks):
        if keyword in tasks[i]:
            arr.append((i,v))         
    return arr

def mark_task_as_done(tasks: list, index: int) -> bool:
    tasks[index] += "✅️"

                         

    
    