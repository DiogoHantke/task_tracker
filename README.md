<h1>Task Tracker CLI</h1>

<p>Task Tracker é um <strong>gerenciador de tarefas via linha de comando (CLI)</strong> simples, desenvolvido como projeto didático do <a href="https://roadmap.sh/projects/task-tracker" target="_blank">Roadmap.sh</a>. O objetivo é praticar fundamentos essenciais de programação, como manipulação de arquivos, tratamento de erros, argumentos de linha de comando e organização de código.</p>

<p>O projeto armazena as tarefas em um arquivo JSON local, permitindo acompanhar tarefas pendentes, em andamento e concluídas.</p>

<h2>Demonstração</h2>
<p>GIF de demonstração do uso do CLI:</p>
<img src="task_tracker.gif" alt="Demonstração do Task Tracker CLI">

<h2>Funcionalidades</h2>
<ul>
    <li>Adicionar novas tarefas</li>
    <li>Atualizar tarefas existentes</li>
    <li>Remover tarefas pelo ID</li>
    <li>Listar todas as tarefas</li>
    <li>Persistência de dados em arquivo JSON</li>
    <li>Criação automática do arquivo de dados caso não exista</li>
    <li>Tratamento básico de erros e casos de borda</li>
</ul>
<p>Cada tarefa possui:</p>
<ul>
    <li>ID único</li>
    <li>Título</li>
    <li>Descrição</li>
    <li>Data de criação</li>
    <li>Prioridade</li>
    <li>Status</li>
</ul>

<h2>Tecnologias utilizadas</h2>
<ul>
    <li>Python 3</li>
    <li>Módulos nativos: <code>json</code>, <code>sys</code>, <code>os</code></li>
</ul>
<p>Este projeto não utiliza frameworks ou bibliotecas externas, mantendo o foco em recursos nativos para fins educacionais.</p>

<h2>Estrutura do projeto</h2>
<pre><code>.
├── task.py        # Script principal do CLI
├── tasks.json     # Arquivo de armazenamento das tarefas (gerado automaticamente)
└── README.md
</code></pre>

<h2>Como executar</h2>
<p>Certifique-se de ter o Python 3 instalado. No diretório do projeto, execute:</p>
<pre><code>python task.py &lt;comando&gt; [argumentos]</code></pre>

<h2>Comandos disponíveis</h2>

<h3>Adicionar tarefa</h3>
<pre><code>python task.py task-add &lt;title&gt; &lt;description&gt; &lt;priority&gt;</code></pre>

<h3>Listar tarefas</h3>
<pre><code>python task.py task-list</code></pre>

<h3>Remover tarefa pelo ID</h3>
<pre><code>python task.py task-drop &lt;id&gt;</code></pre>

<h3>Atualizar tarefa</h3>
<pre><code>python task.py task-update</code></pre>

<h3>Exibir ajuda</h3>
<pre><code>python task.py task-help</code></pre>

<h2>Decisões de projeto</h2>
<ul>
    <li><strong>IDs não são reutilizados:</strong> mesmo após a exclusão de uma tarefa, novos IDs continuam incrementando.</li>
    <li><strong>Persistência simples:</strong> uso de JSON para facilitar leitura, depuração e portabilidade.</li>
    <li><strong>CLI puro:</strong> o programa opera exclusivamente por argumentos de linha de comando, sem menus interativos.</li>
</ul>

<h2>Limitações conhecidas</h2>
<ul>
    <li>O comando de atualização ainda está em desenvolvimento</li>
    <li>Interface exclusivamente textual</li>
    <li>Projeto focado em aprendizado, não em uso produtivo</li>
</ul>

<h2>Objetivo educacional</h2>
<p>Este projeto foi desenvolvido como <strong>projeto didático do Roadmap.sh</strong>, com foco em:</p>
<ul>
    <li>Lógica de programação</li>
    <li>Organização de código</li>
    <li>Manipulação de arquivos</li>
    <li>Pensamento de engenharia de software</li>
    <li>Construção de aplicações CLI</li>
</ul>

<h2>Licença</h2>
<p>Este projeto é livre para estudo, modificação e uso educacional.</p>
