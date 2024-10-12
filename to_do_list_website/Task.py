class Task:
    number = 1  # Task ID counter
    li = []     # List to hold tasks

    # Method to add a task
    def add_task(self, task, priority):
        d = {
            "id": self.number,
            "task": task,
            "priority": priority,
            "is_complated": False  # Default: task not completed
        }
        self.number += 1  # Increment ID for the next task
        self.li.append(d)  # Add the task to the list
        return True
         
    # Find the task by ID
    def is_valid(self, id):
        for ind, l in enumerate(self.li):
            if id == l["id"]:
                return ind + 1
        return False

    # Method to edit a task
    def edit_task(self, ind, task, priority, is_completed):
        # Update values if provided
        if task:
            self.li[ind]["task"] = task
        if priority:
            self.li[ind]["priority"] = priority
        self.li[ind]["is_complated"] = is_completed
        return True

    # Method to delete a task
    def delete_task(self, ind):
        if self.li.pop(ind):  # Remove task from the list
            return True
        return False

    # Method to show number of completed tasks
    def completed_tasks(self):
        if not self.li:  
            return False
        # Using lambda 
        completed_count = len(list(filter(lambda x: x["is_complated"] == 1, self.li)))
        return completed_count

    # Method to display all tasks
    def display_tasks(self):
        if not self.li:
            return False
        else:
            return self.li
    
    def display_task(self, ind):
        task = self.li[ind]
        if not task:
            return False
        else:
            return task

# Main interaction loop
# def main():
#     task_manager = Task()  # Create a Task instance
#     while True:
#         print("\nTask Manager Menu:")
#         print("1. Add Task")
#         print("2. Edit Task")
#         print("3. Delete Task")
#         print("4. View All Tasks")
#         print("5. View All Completed Tasks")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")
#         if choice == '1':
#             task = input("Enter the task description: ")
#             try: # this code may throw an exception
#                 priority = int(input("Enter the task priority number from 1 to 3: \n 1:(high priority) \n 2: (medium priority) \n 3: (low priority) \n"))
#             except:
#                 print("Please make sure you have entered priority number")
#             else: # this code block will execute if try does not throw an exception
#                 if priority in range(1,4):
#                     if task_manager.add_task(task, priority):
#                         print(f"Task '{task}' added successfully with ID: {task_manager.li[-1]['id']}")
#                 else:
#                     print("Please enter a valid task and priority.")
#         elif choice == '2':
#             try:
#                 id = int(input("Enter the task ID to edit: "))
#                 ind = task_manager.is_valid(id)
#                 if ind > 0:
#                     new_task = input("Enter new task description (leave blank to keep current): ")
#                     new_priority = input("Enter new priority (leave blank to keep current): ")
#                     new_is_completed = input("Enter 1 for completed or 2 for not completed (leave blank to keep current): ")
#                     if task_manager.edit_task(ind - 1, new_task, new_priority, new_is_completed):
#                         print(f"Task ID {id} has been updated.")
#                 else:
#                     print("Task not found with the provided ID.")
#             except ValueError:
#                 print("Please enter a valid ID.")
#         elif choice == '3':
#             try:
#                 id = int(input("Enter the task ID to delete: "))
#                 ind = task_manager.is_valid(id)
#                 if ind > 0:
#                     if task_manager.delete_task(ind -1):
#                         print(f"Task ID {id} has been deleted.")
#                     else:
#                         print("Task not found with the provided ID.")
#                 else:
#                     print("Task not found with the provided ID.")
#             except ValueError:
#                 print("Please enter a valid ID.")
#         elif choice == '4':
#             tasks = task_manager.display_tasks()
#             if tasks:
#                 print("Current tasks:")
#                 for task in tasks:
#                     status = "Completed" if task["is_complated"] == 1 else "Not Completed"
#                     print(f"ID: {task['id']}, Task: {task['task']}, Priority: {task['priority']}, Status: {status}")
#             else:
#                 print("No tasks available.")
#         elif choice == '5':
#             completed_count = task_manager.completed_tasks()
#             if completed_count:
#                 print("Total of completed tasks is:", completed_count)
#             else:
#                 print("No tasks available.")
#         elif choice == '6':
#             print("Exiting task manager.")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 6.")

# # Start the interactive task manager
# #main()