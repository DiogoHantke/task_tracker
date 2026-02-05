import json, sys, os
from tabulate import tabulate 

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

def write_json(tasks : dict):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "tasks.json")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

    except json.decoder.JSONDecodeError:
        print("arquivo corrompido.")

def task_add():
    tasks, new_id = read_json(), 1

    if tasks is None: #melhorar tratamento de erro no arquivo
        return None

    if tasks['tasks'] == []:
        new_id = 1
    else:
        list_id = [task['id'] for task in tasks['tasks']]
        new_id = max(list_id)+1

    title = input("Digite o título: ").strip()
    description = input("Digite a descrição: ").strip()
    priority = input("Digite a prioridade (Baixa, Média, Alta): ").strip()

    description_treated = []

    tasks['tasks'].append({
        'id' : new_id,
        'title' : title,
        'description' : description,
        'create_date' : os.popen('date /t').read().strip(),
        'priority' : priority,
        'status' : 'Pending'
    })

    write_json(tasks)
    task_list()

def task_help():
    print("""TASK - Gerenciador de Tarefas via Linha de Comando

Uso:
    python task.py <comando> [argumentos]

Comandos disponíveis:

    task-add
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
    
def task_update():
    ...

def task_drop(argv : int): #colocar um tratamento se caso nao existir o id que o user colocou
    tasks = read_json()

    for index, id in enumerate(tasks['tasks']):
        if argv == id['id']:
            del(tasks['tasks'][index])

    write_json(tasks)
    task_list()

def task_list():
    tasks = read_json()

    if tasks is not None:
        print(display_task(tasks))

def display_task(tasks : dict):

    tasks_list, data = [data for data in tasks['tasks']], []

    for index in range(len(tasks_list)):
        data.append(tasks_list[index].values())
    
    headers = ["id", "title", "description", "create_date", "priority", "status"]
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")

    return table

if __name__ == "__main__":
    os.system('cls')

    argv = sys.argv

    commands = {
        "task-add"    : lambda: task_add(),
        "task-update" : lambda: task_update(),
        "task-drop"   : lambda: task_drop(int(argv[2])),
        "task-list"   : lambda: task_list(),
        "task-help"   : lambda: task_help(),
        "task-exit"   : lambda: exit()
    }

    try:
        commands[argv[1].lower()]() if argv[1].lower() in commands else print("ErrorCommand: Not found")
    except IndexError:
        print("O comando não existe, tente task-list, task-add, task-update") 
