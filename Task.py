class Task:
    number = 1  # Task ID counter
    li = []     # List to hold tasks

    # Method to add a task
    def add_task(self):
        task = input("Enter the task description: ")
        try: # this code may throw an exception
         priority = int(input("Enter the task priority number from 1 to 3: \n 1:(high priority) \n 2: (medium priority) \n 3: (low priority) \n"))
        except:
            print("Please make sure you have entered priority number")
        else: # this code block will execute if try does not throw an exception
         if priority in range(1,4):
            d = {
                "id": self.number,
                "task": task,
                "priority": priority,
                "is_complated": 2  # Default: task not completed
            }
            self.number += 1  # Increment ID for the next task
            self.li.append(d)  # Add the task to the list
            print(f"Task '{task}' added successfully with ID: {d['id']}")
         else:
            print("Please enter a valid task and priority.")

    # Method to edit a task
    def edit_task(self):
        try:
            id = int(input("Enter the task ID to edit: "))
        except ValueError:
            print("Please enter a valid ID.")
            return

        # Find the task by ID
        for ind, l in enumerate(self.li):
            if id == l["id"]:
                new_task = input("Enter new task description (leave blank to keep current): ")
                new_priority = input("Enter new priority (leave blank to keep current): ")
                new_is_completed = input("Enter 1 for completed or 2 for not completed (leave blank to keep current): ")

                # Update values if provided
                if new_task:
                    self.li[ind]["task"] = new_task
                if new_priority.isdigit():
                    self.li[ind]["priority"] = int(new_priority)
                if new_is_completed in ['1', '2']:
                    self.li[ind]["is_complated"] = int(new_is_completed)

                print(f"Task ID {id} has been updated.")
                return

        print("Task not found with the provided ID.")

    # Method to delete a task
    def delete_task(self):
        try:
            id = int(input("Enter the task ID to delete: "))
        except ValueError:
            print("Please enter a valid ID.")
            return

        for ind, l in enumerate(self.li):
            if id == l["id"]:
                self.li.pop(ind)  # Remove task from the list
                print(f"Task ID {id} has been deleted.")
                return
        
        print("Task not found with the provided ID.")

    # Method to show number of completed tasks
    def completed_tasks(self):
        if not self.li:  
            print("No tasks available.")
            return

        # Using lambda 
        completed_count = len(list(filter(lambda x: x["is_complated"] == 1, self.li)))

        print("Total of completed tasks is:", completed_count)

    # Method to display all tasks
    def display_tasks(self):
        if not self.li:
            print("No tasks available.")
        else:
            print("Current tasks:")
            for task in self.li:
                status = "Completed" if task["is_complated"] == 1 else "Not Completed"
                print(f"ID: {task['id']}, Task: {task['task']}, Priority: {task['priority']}, Status: {status}")

# Main interaction loop
def main():
    task_manager = Task()  # Create a Task instance
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View All Completed Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            task_manager.add_task()
        elif choice == '2':
            task_manager.edit_task()
        elif choice == '3':
            task_manager.delete_task()
        elif choice == '4':
            task_manager.display_tasks()
        elif choice == '5':
            task_manager.completed_tasks()
        elif choice == '6':
            print("Exiting task manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Start the interactive task manager
main()