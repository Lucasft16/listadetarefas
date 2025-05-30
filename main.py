from flask import Flask, request, redirect, render_template
from package.models.projeto import Projeto
from package.models.tarefa import Tarefa, TarefaImportante
from package.controllers.db import ProjetoDB

app = Flask(__name__)
db = ProjetoDB()
projeto = db.carregar()

@app.route('/')
def index():
    return render_template('index.html', projeto=projeto)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form['titulo']
    desc = request.form['desc']
    importante = 'importante' in request.form

    tarefa = TarefaImportante(titulo, desc) if importante else Tarefa(titulo, desc)
    projeto.adicionar_tarefa(titulo, tarefa)
    db.salvar(projeto)
    return redirect('/')

@app.route('/concluir', methods=['POST'])
def concluir():
    titulo = request.form['titulo']
    if titulo in projeto.tarefas:
        projeto.tarefas[titulo].alternar_status()
    db.salvar(projeto)
    return redirect('/')

@app.route('/remover', methods=['POST'])
def remover():
    projeto.remover_tarefa(request.form['titulo'])
    db.salvar(projeto)
    return redirect('/')

@app.route('/toggle_prioridade', methods=['POST'])
def toggle_prioridade():
    titulo = request.form['titulo']
    if titulo in projeto.tarefas:
        tarefa = projeto.tarefas[titulo]
        desc = tarefa.desc
        concluido = tarefa.concluido

        if isinstance(tarefa, TarefaImportante):
            nova_tarefa = Tarefa(titulo, desc, concluido)
        else:
            nova_tarefa = TarefaImportante(titulo, desc, concluido)

        projeto.tarefas[titulo] = nova_tarefa
        db.salvar(projeto)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
