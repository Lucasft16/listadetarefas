from listatarefas.package.models.projeto import Projeto

def workspace():
    # Criar um projeto
    projeto = Projeto("Meu Projeto de Teste")
    print(f"Projeto criado: {projeto.titulo}")

    # Adicionar tarefas
    projeto.adicionar_tarefa("Estudar Python", "Revisar classes e objetos")
    projeto.adicionar_tarefa("Fazer exercícios", "Implementar mini projeto em Flask")

    # Exibir tarefas antes de concluir
    print("\nTarefas antes de concluir:")
    for tarefa in projeto.tarefas.values():
        print(tarefa.exibir())

    # Concluir uma tarefa
    projeto.tarefas["Estudar Python"].concluir()


    # Exibir tarefas depois de concluir
    print("\nTarefas depois de concluir uma:")
    for tarefa in projeto.tarefas.values():
        print(tarefa.exibir())

    projeto.remover_tarefa("Estudar Python")
    print("\n")

    for tarefa in projeto.tarefas.values():
        print(tarefa.exibir())

if __name__ == "__main__":
    workspace()
