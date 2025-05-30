from package.models.tarefa import Tarefa, TarefaImportante

class Projeto:
    def __init__(self, titulo):
        self.titulo = titulo
        self.tarefas = {}

    def adicionar_tarefa(self, titulo, tarefa):
        self.tarefas[titulo] = tarefa

    def remover_tarefa(self, titulo):
        if titulo in self.tarefas:
            self.tarefas.pop(titulo)
    
    def tarefas_ordenadas(self):
        return sorted(self.tarefas.values(), key=lambda t: isinstance(t, TarefaImportante), reverse=True)

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "tarefas": [tarefa.to_dict() for tarefa in self.tarefas.values()]
        }

    @staticmethod
    def from_dict(data):
        projeto = Projeto(data["titulo"])
        for tarefa_dict in data.get("tarefas", []):
            tarefa = Tarefa.from_dict(tarefa_dict)
            projeto.tarefas[tarefa.titulo] = tarefa
        return projeto
