import json, sys, os, datetime
from tabulate import tabulate 

RED    = "\033[31m"
GREEN  = "\033[32m"
RESET  = "\033[0m"

def read_json():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            return tasks

    except FileNotFoundError:
        
        with open(file_path, "w", encoding="utf-8") as file:
            tasks = {"tasks":[]}
            json.dump(tasks, file, ensure_ascii=False, indent=2) #estudar mais
            print(GREEN + "Arquivo de tarefas criado, adicione sua tarefa" + RESET)
            return tasks
        
    except json.JSONDecodeError:
        
        print(RED + "arquivo corrompido. " + RESET)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({"tasks": []}, file, ensure_ascii=False, indent=2)
        return None

def write_json(tasks : dict):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def task_add(argv : list):
    tasks, new_id = read_json(), 1

    argv_sep = argv[2:]

    if tasks is None: #melhorar tratamento de erro no arquivo
        return None

    if tasks['tasks'] == []:
        new_id = 1
    else:
        list_id = [task['id'] for task in tasks['tasks']]
        new_id = max(list_id)+1

    title = argv_sep[0].strip()
    description = argv_sep[1].strip()
    priority = argv_sep[2].strip()

    tasks['tasks'].append({
        'id' : new_id,
        'title' : description_treated(title),
        'description' : description_treated(description),
        'create_date' : get_now(),
        'update_date' : get_now(),
        'priority' : priority,
        'status' : 'Pending'
    })

    write_json(tasks)
    task_list()

def task_update(argv : list):
    tasks, args = read_json(), argv[2:]

    if tasks is None:
        return 
    
    for index, id_task in enumerate(tasks['tasks']):

        if int(args[0]) == int(id_task['id']):
            tasks['tasks'][index]['priority'] = args[1]
            tasks['tasks'][index]['update_date'] = get_now()
            break
        
        elif index >= len(tasks['tasks'])-1:
            print(RED + "Id não existe." + RESET)
            return 
        
    write_json(tasks)
    task_list()
    return

def task_drop(argv : int): #colocar um tratamento se caso nao existir o id que o user colocou
    tasks, argv = read_json(), int(argv[2])

    if tasks is None:
        return 

    for index, id_task in enumerate(tasks['tasks']):

        if argv == int(id_task['id']):
            del(tasks['tasks'][index])
            break
        
        elif index >= len(tasks['tasks'])-1:
            print(RED + "Id não existe." + RESET)
            return 
        
    write_json(tasks)
    task_list()
    return None

def task_list():
    tasks = read_json()

    if tasks is not None:
        print(display_task(tasks))

def display_task(tasks : dict):

    tasks_list, data = [data for data in tasks['tasks']], []

    for index in range(len(tasks_list)):
        data.append(tasks_list[index].values())
    
    headers = ["id", "title", "description", "create_date", "update_date", "priority", "status"]
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")

    if tasks['tasks'] == []:
        print(RED + 'sem tarefas para exibir, adicione uma tarefa.' + RESET)
        exit()
    else:
        return table

def task_help():
    print(GREEN + "TASK - Gerenciador de Tarefas via Linha de Comando" + RESET + """

Uso:
    python task.py <comando> [argumentos]

Comandos disponíveis:

    task-add "title" "description" "priority"
        Adiciona uma nova tarefa.
        Solicita título, descrição e prioridade.

    task-list
        Exibe todas as tarefas cadastradas.

    task-drop <id>
        Remove a tarefa correspondente ao ID informado.

    task-update
        Atualiza uma tarefa existente.
        (Comando em desenvolvimento)

    task-help
        Exibe esta tela de ajuda.

    task-exit
        Encerra o programa.

Observações:
    - O arquivo tasks.json é criado automaticamente se não existir.
    - Cada tarefa possui um ID único.
    - Comandos inválidos exibem uma mensagem de erro.

Exemplos:
    python task.py task-add
    python task.py task-list
    python task.py task-drop 1
""")
    
def description_treated(description : str):
    description_treated, num, number = [], 0, 50

    for string in description.split():
        num+=len(string)+1
        if num >= number:
            num = len(string)+1
            description_treated.append(f"\n{string}")
        else:
            description_treated.append(string)

    return ' '.join(description_treated)


def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    clear_screen()

    argv = sys.argv

    commands = {
        "task-add"    : lambda: task_add(argv),
        "task-update" : lambda: task_update(argv),
        "task-drop"   : lambda: task_drop(argv),
        "task-list"   : lambda: task_list(),
        "task-help"   : lambda: task_help(),
        "task-exit"   : lambda: exit()
    }

    try:
        commands[argv[1].lower()]() if argv[1].lower() in commands else task_help()

    except IndexError:
        print(RED + "ERROR: command not found\n" + RESET)
        task_help() 