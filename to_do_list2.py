


def main():
    task =[]

while True:
    print("\n=======  TO_DO_LIST  =======")
    print("1. Add Task")
    print("2. Show Task")
    print("3. Mark Task as Done")
    print("4.  Exit")

    choice = input("Enter your choice")

    if choice == '1':
        print()
        n_task =int(input("How may task want to add: "))

        for i in range(n_task):
            task =input("Enter the task: ")
            task.append({"task":task,"done": True})
            print("Task added")

    elif choice =='2':
        print("\nTask:")
        for index, task in enumerate(task):
            status = "Done" if task["done"] else "NOt Done"
            print(f"{index+1}.{task['task']}-{status}")

    elif choice == '3':
        task_index= int(input("Enter the task number to mark as done :")) -1
        if 0 <=  task_index < len(task):
            task[task_index]["done"] =True  
            print("Task Markes as done!")
        else:
            print("Invalid task number.")

    elif  choice =='4':
        print("Exiting the TO-Do List .")   
        break
        
    else:
        print("Invalid choice.please try again.")


if __name__ == "__main__":   
    main()
   

