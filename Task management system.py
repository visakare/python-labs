# Створіть словник, де ключі - це назви задач, а значення - їх статус ("виконано", "в процесі", "очікує").
# Напишіть функції для додавання, видалення та зміни статусу задач. Додатково: створіть список задач, які мають статус "очікує".


# Функція для додавання нового завдання
def add_task(tasks_dict, task_name, status = 'expects'):
    if task_name in tasks_dict:
        print(f"Error: Task: '{task_name}' already exists.")
    else:
        tasks_dict[task_name] = status
        print(f"Task '{task_name}' added with status '{status}'.")

# Функція для видалення завдання
def remove_task(tasks_dict, task_name):
    if task_name in tasks_dict:
        del tasks_dict[task_name]
        print(f"Task '{task_name}' removed.")
    else:
        print(f"Error: Task: '{task_name}' not found.")

# Функція для оновлення статусу завдань
def update_task_status(tasks_dict, task_name, new_status):
    if task_name in tasks_dict:
        tasks_dict[task_name] = new_status
        print(f"Task '{task_name}' status updated to '{new_status}'.")
    else:
        print(f"Error: Task: '{task_name}' not found.")

# Словник задач
tasks= {
    'Develop a new strategy for the project':'in progress',
    'Check industry news':'done',
    'Respond to client emails':'expects',
    'Prepare a presentation for tomorrow\'s meeting':'done',
}
print(tasks, "\n")

# Додавання нового завдання
add_task(tasks, 'Update the client database', 'in progress')
add_task(tasks, 'Prepare a list of questions for the meeting')
print(tasks)
add_task(tasks, 'Update the client database')
print(tasks, "\n")

# Видалення завдання
remove_task(tasks, 'Check industry news')
print(tasks)
remove_task(tasks, 'Analyze competitors')
print(tasks, "\n")

# Оновлення статусу завдання
update_task_status(tasks, 'Develop a new strategy for the project', 'done')
print(tasks)
update_task_status(tasks, 'Check industry news', 'in progress')
print(tasks, "\n")

# Список задач, які мають статус "очікує"
list_pending_tasks = [task_name for task_name, status in tasks.items() if status == 'expects']
print("List of tasks with status expects:", list_pending_tasks)
