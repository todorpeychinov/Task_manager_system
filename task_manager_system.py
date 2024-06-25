import json
from datetime import datetime


def prepare_file_for_using(tasks):
    '''
    Preparing the list of tasks from the json file to be used in the program.
    :param tasks: tasks list
    :return: ready tasks list for the program
    '''
    for task in tasks:
        date_as_str = task['deadline']
        date = datetime.strptime(date_as_str, '%Y-%m-%d %H:%M:%S')
        task['deadline'] = date
    return tasks


def prepare_file_for_saving(tasks):
    '''
    Preparing the list of tasks for saving in a json file.
    :param tasks: tasks_list
    :return: ready_to_be_saved_list
    '''
    for task in tasks:
        date = task['deadline']
        date_as_string = str(date)
        task['deadline'] = date_as_string
    return tasks

def is_valid_date(date):
    '''
    Date input validation
    :param date: date_input
    :return: True or False
    '''
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_valid_priority(priority):
    if (
            priority == 'low'
            or priority == 'medium'
            or priority == 'high'
    ):
        return True
    return False


def check_task_index(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return tasks.index(task)


def is_existing_id(tasks, id):
    '''
    Check if task id is in the tasks list
    :param tasks: The current list of tasks
    :param id: The id to be checked
    :return: True or False
    '''
    for task in tasks:
        if task['id'] == id:
            return True
    return False


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """
    flag = is_existing_id(tasks, task['id'])

    while flag:
        print('\nCurrent id already exists')
        new_id = int(input('Enter new task id: '))
        task['id'] = new_id
        flag = is_existing_id(tasks, task['id'])

    while not is_valid_date(task['deadline']):
        print('\nInvalid date format')
        date_string = input('Enter valid date format (YYYY-MM-DD): ')
        task['deadline'] = date_string

    while not is_valid_priority(task['priority']):
        print('\nInvalid priority format')
        priority_string = input('Enter valid priority format: (low, medium or high): ')
        task['priority'] = priority_string

    date_as_string = task['deadline']
    date_list = date_as_string.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    x = datetime(year, month, day)
    task['deadline'] = x

    tasks.append(task)

    return tasks


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """

    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    task_index = check_task_index(tasks, task_id)
    tasks.pop(task_index)
    return tasks


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """
    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    index = check_task_index(tasks, task_id)
    tasks[index] = updated_task

    return tasks


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """

    if is_existing_id(tasks, task_id):
        task_index = check_task_index(tasks, task_id)
        return tasks[task_index]
    else:
        print('\nTask not found')
        return None


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """
    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    index = check_task_index(tasks, task_id)
    tasks[index]['priority'] = priority

    return tasks


def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """
    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    index = check_task_index(tasks, task_id)
    tasks[index]['deadline'] = deadline

    return tasks


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """
    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    index = check_task_index(tasks, task_id)
    tasks[index]['completed'] = True

    return tasks


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """

    while not is_existing_id(tasks, task_id):
        print('\nTask not found')
        task_id = int(input('Enter a valid task id: '))

    index = check_task_index(tasks, task_id)
    tasks[index]['description'] = description

    return tasks


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """

    list_of_results = []
    for task in tasks:
        if keyword in task['description']:
            list_of_results.append(task)
    return list_of_results


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """
    while not is_valid_priority(priority):
        print('\nInvalid priority format')
        priority = input('Enter valid priority format: (low, medium or high): ')

    priority_list = [task for task in tasks if task['priority'] == priority]
    return priority_list


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """
    tasks_with_status = []

    if status == 'completed':
        tasks_with_current_status = [task for task in tasks if task['completed'] == True]
    else:
        tasks_with_current_status = [task for task in tasks if not task['completed'] == False]
    return tasks_with_current_status


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """
    while not is_valid_date(deadline):
        print('\nInvalid deadline format')
        deadline = input('Enter valid deadline format: (YYYY-MM-DD): ')

    deadline = datetime.strptime(deadline, '%Y-%m-%d')
    tasks_with_current_deadline = [task for task in tasks if task['deadline'] == deadline]
    return tasks_with_current_deadline


def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """

    return len(tasks)


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """

    counter = 0
    for task in tasks:
        if task['completed'] == True:
            counter += 1
    return counter


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """
    counter = 0
    for task in tasks:
        if task['completed'] == False:
            counter += 1
    return counter


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """

    completed_tasks = count_completed_tasks(tasks)
    pending_tasks = count_pending_tasks(tasks)
    total_tasks = completed_tasks + pending_tasks
    summary = {'completed': completed_tasks, 'pending': pending_tasks, 'total': total_tasks}
    return summary


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """
    ready_to_save_list = prepare_file_for_saving(tasks)
    with open(file_path, 'w') as fout:
        json.dump(ready_to_save_list, fout)


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """

    with open(file_path, 'r') as f:
        loaded_data = json.load(f)
    return prepare_file_for_using(loaded_data)


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """
    tasks = sorted(tasks, key=lambda task: task['deadline'])
    return tasks


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """

    list_of_low_priority_tasks = [task for task in tasks if task['priority'] == 'low']
    list_of_medium_priority_tasks = [task for task in tasks if task['priority'] == 'medium']
    list_of_high_priority_tasks = [task for task in tasks if task['priority'] == 'high']

    tasks = list_of_low_priority_tasks + list_of_medium_priority_tasks + list_of_high_priority_tasks
    return tasks


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': int(input("Enter task ID: ")),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): "),
                'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                'completed': False
            }
            tasks = add_task(tasks, task)
            print("Task added successfully.")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id)
            print("Task removed successfully.")
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            updated_task = {
                'description': input("Enter new task description: "),
                'priority': input("Enter new task priority (low, medium, high): "),
                'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }
            tasks = update_task(tasks, task_id, updated_task)
            print("Task updated successfully.")
        elif choice == '4':
            task_id = int(input("Enter task ID to get: "))
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            task_id = int(input("Enter task ID to set priority: "))
            priority = input("Enter new priority (low, medium, high): ")
            tasks = set_task_priority(tasks, task_id, priority)
            print("Task priority set successfully.")
        elif choice == '6':
            task_id = int(input("Enter task ID to set deadline: "))
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks = set_task_deadline(tasks, task_id, deadline)
            print("Task deadline set successfully.")
        elif choice == '7':
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = mark_task_as_completed(tasks, task_id)
            print("Task marked as completed.")
        elif choice == '8':
            task_id = int(input("Enter task ID to set description: "))
            description = input("Enter new description: ")
            tasks = set_task_description(tasks, task_id, description)
            print("Task description set successfully.")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

