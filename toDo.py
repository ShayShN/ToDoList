

todo_list = ["Buy milk", "Do homework", "Buy bread", "Buy"]

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

                         
def main() -> None:
    while True:
        status_user = get_user_choice()
        if status_user == "1":
            user_task = input("enter a mission: ")
            add_task(todo_list, user_task)
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
                user_edit_task = input("enter a update mission: ")
                edit_task(todo_list, user_index, user_edit_task)
            else:
                print("!!!wrong index!!!")
        elif status_user == "6":
            user_search = input("enter a word to search: ")
            print(search_tasks(todo_list, user_search))
        elif status_user == "7":
            user_done =get_task_index_from_user()
            if user_done in range(len(todo_list)):
                mark_task_as_done(todo_list, user_done)
        elif status_user == "5":
             break  
main()
# if __name__=="__main":      
#     main()
    
    