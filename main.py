from toDo import get_task_index_from_user,get_user_choice,add_task,show_all_tasks,delete_task,edit_task,search_tasks,mark_task_as_done


todo_list = ["Buy milk", "Do homework", "Buy bread", "Buy"]

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

if __name__=="__main__":      
    main()