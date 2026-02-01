import json, time, sys, os
from tabulate import tabulate

def read_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
        print(tasks)

    except FileNotFoundError:
        with open(file_path, "w", encoding="utf-8") as file:
            tasks = {
                
            }
            json.dump(tasks, file, ensure_ascii=False, indent=2) #estudar mais
            print("Arquivo de tarefas criado, adicione sua tarefa")
            return None
    return None


def write_json(tasks : dict):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def task_add():
    ...

def task_update():
    ...

def task_drop():
    ...

def task_list():
    tasks = read_json()

    if tasks is None:
        print("Não há nenhuma tarefa na lista")

def display_task():
    ...

if __name__ == "__main__":
    os.system('cls')
    argv = sys.argv

    commands = {
        "task-add"    : task_add,
        "task-update" : task_update,
        "task-drop"   : task_drop,
        "task-list"   : task_list,
        "task-exit"   : exit
    }

    try:
        commands[argv[1].lower()]() if argv[1].lower() in commands else print("ErrorCommand: Not found")
    except IndexError:
        print("No command provided. Use one of: task-add, task-list, ...")
    