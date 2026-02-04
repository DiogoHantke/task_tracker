import json, sys, os
from tabulate import tabulate 
#---------------------------------------------------------------------------------------
def read_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")
    try:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                tasks = json.load(file)
                return tasks

        except FileNotFoundError:
            with open(file_path, "w", encoding="utf-8") as file:
                tasks = {"tasks":[]}
                json.dump(tasks, file, ensure_ascii=False, indent=2) #estudar mais
                print("Arquivo de tarefas criado, adicione sua tarefa")
                return tasks

    except json.decoder.JSONDecodeError:
        print("arquivo corrompido. ")
        return None
#---------------------------------------------------------------------------------------

def write_json(tasks : dict):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

    except json.decoder.JSONDecodeError:
        print("arquivo corrompido.")
#---------------------------------------------------------------------------------------
def task_add():
    tasks, new_id = read_json(), 0

    if tasks is None: #melhorar tratamento de erro no arquivo
        return None

    list_id = [task['id'] for task in tasks['tasks']]

    if tasks['tasks'] == []:
        new_id = 0
    else:
        new_id = max(list_id)+1

    #adicionar algoritmo de quebra de linha
    
    tasks['tasks'].append({
        'id' : new_id,
        'title' : input("Digite o título: "),
        'description' : input("Digite a descrição: "),
        'create_date' : os.popen('date /t').read().strip(),
        'priority' : input("Digite a prioridade (Baixa, Média, Alta): "),
        'status' : 'Pending'
    })
    
    write_json(tasks)
#---------------------------------------------------------------------------------------
    
def task_update():
    ...

def task_drop():
    ...
#---------------------------------------------------------------------------------------
def task_list():
    tasks = read_json()

    if tasks is not None:
        print(display_task(tasks))
#---------------------------------------------------------------------------------------
def display_task(tasks : dict):

    tasks_list, data = [data for data in tasks['tasks']], []

    for index in range(len(tasks_list)):
        data.append(tasks_list[index].values())
    
    headers = ["id", "title", "description", "create_date", "priority", "status"]
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")

    return table
#---------------------------------------------------------------------------------------
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
        print("O comando não existe, tente task-list, task-add, task-update")
    