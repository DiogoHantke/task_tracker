# Task Tracker CLI

Um **gerenciador de tarefas via linha de comando (CLI)** simples e direto, desenvolvido como projeto didático do [Roadmap.sh](https://roadmap.sh/projects/task-tracker) para praticar fundamentos essenciais de programação como manipulação de arquivos, tratamento de erros, argumentos de linha de comando e organização de código.

O projeto armazena as tarefas em um arquivo JSON local, permitindo acompanhar o que precisa ser feito, o que está em andamento e o que já foi concluído.

---

## 📸 Demonstração

> GIF de demonstração do uso do CLI (em breve):

```markdown
![Demonstração do Task Tracker CLI](./assets/demo.gif)
```

*(Substitua o caminho pelo local correto do GIF quando adicioná-lo ao repositório.)*

---

## 🚀 Funcionalidades

* Adicionar novas tarefas
* Atualizar tarefas existentes
* Remover tarefas pelo ID
* Listar todas as tarefas
* Persistência de dados em arquivo JSON
* Criação automática do arquivo de dados caso não exista
* Tratamento básico de erros e casos de borda

Cada tarefa possui:

* ID único
* Título
* Descrição
* Data de criação
* Prioridade
* Status

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* Módulos nativos:

  * `json`
  * `sys`
  * `os`

> ⚠️ Observação: este projeto não utiliza frameworks ou bibliotecas externas, seguindo o objetivo educacional de trabalhar apenas com recursos nativos.

---

## 📂 Estrutura do projeto

```text
.
├── task.py        # Script principal do CLI
├── tasks.json     # Arquivo de armazenamento das tarefas (gerado automaticamente)
└── README.md
```

---

## ▶️ Como executar

Certifique-se de ter o **Python 3** instalado.

No diretório do projeto, execute:

```bash
python task.py <comando> [argumentos]
```

---

## 📌 Comandos disponíveis

### Adicionar tarefa

```bash
python task.py task-add
```

### Listar tarefas

```bash
python task.py task-list
```

### Remover tarefa pelo ID

```bash
python task.py task-drop <id>
```

### Atualizar tarefa

```bash
python task.py task-update
```

### Exibir ajuda

```bash
python task.py task-help
```

---

## 🧠 Decisões de projeto

* **IDs não são reutilizados**: mesmo após a exclusão de uma tarefa, novos IDs continuam incrementando para garantir consistência e evitar ambiguidades.
* **Persistência simples**: uso de JSON para facilitar leitura, depuração e portabilidade.
* **CLI puro**: o programa opera exclusivamente por argumentos de linha de comando, sem menus interativos.

---

## ⚠️ Limitações conhecidas

* O comando de atualização ainda está em desenvolvimento
* Interface exclusivamente textual
* Projeto focado em aprendizado, não em uso produtivo

---

## 🎯 Objetivo educacional

Este projeto foi desenvolvido como **projeto didático do Roadmap.sh**, com fins de estudo e prática, com foco em:

* Lógica de programação
* Organização de código
* Manipulação de arquivos
* Pensamento de engenharia de software
* Construção de aplicações CLI

---

## 📄 Licença

Este projeto é livre para estudo, modificação e uso educacional.