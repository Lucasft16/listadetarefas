class Tarefa:
    def __init__(self, titulo, desc, concluido=False):
        self.titulo = titulo
        self.desc = desc
        self.concluido = concluido

    def concluir(self):
        self.concluido = True

    def exibir(self):
        status = "✅" if self.concluido else "❌"
        return f"[{status}] <strong>{self.titulo}</strong>: {self.desc}"
    
    def alternar_status(self):
        self.concluido = not self.concluido

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "desc": self.desc,
            "concluido": self.concluido,
            "importante": False
        }

    @staticmethod
    def from_dict(data):
        if data.get("importante"):
            return TarefaImportante(data["titulo"], data["desc"], data.get("concluido", False))
        return Tarefa(data["titulo"], data["desc"], data.get("concluido", False))


class TarefaImportante(Tarefa):
    def __init__(self, titulo, desc, concluido=False):
        super().__init__(titulo, desc, concluido)

    def exibir(self):
        status = "✅" if self.concluido else "❌"
        return f"🔥[{status}] <strong>{self.titulo}</strong>: {self.desc}"

    def to_dict(self):
        base = super().to_dict()
        base["importante"] = True
        return base
