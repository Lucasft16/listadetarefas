import os
import json
from package.models.projeto import Projeto

class ProjetoDB:
    def __init__(self, filename='projeto.json'):
        self.__filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 
            'db',  
            filename 
        )

    def salvar(self, projeto):
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(projeto.to_dict(), f, indent=4, ensure_ascii=False)

    def carregar(self):
        if not os.path.exists(self.__filename):
            return Projeto("Lista de Tarefas")
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Projeto.from_dict(data)
