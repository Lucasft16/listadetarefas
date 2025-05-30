## Lista de Tarefas

## 📌 Descrição

Este é um sistema simples de gerenciamento de tarefas desenvolvido com Python e Flask. O projeto permite adicionar, concluir, remover e priorizar tarefas.

## ✅ Funcionalidades

- Adicionar tarefas normais ou importantes
- Concluir ou desmarcar tarefas
- Remover tarefas
- Alternar entre tarefa normal e importante

## ⚙️ Como Executar

1. Clone este repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
python main.py
```

4. Acesse no navegador:

```
http://127.0.0.1:5000/
```

## 📦 Requisitos

- Python 3.8+
- pip
- Navegador moderno

## 🧾 Casos de Uso

**Caso de Uso 1: Adicionar Tarefa**

- Ator principal: Usuário
- Objetivo: Permitir que o usuário registre uma nova tarefa no sistema.
- Pré-condições: O sistema está rodando.
- Pós-condições: A tarefa é salva e exibida na interface.
- Fluxo principal:
- O usuário clica no botão “Adicionar Tarefa”.
- O usuário preenche o título e a descrição da tarefa.
- O usuário clica em “Adicionar”.
- O sistema cria a tarefa.
- A tarefa é adicionada ao projeto.
- O projeto é salvo no arquivo JSON.
- A interface é atualizada com a nova tarefa.

**Caso de Uso 2: Concluir ou Desmarcar Tarefa**

- Ator principal: Usuário
- Objetivo: Permitir que o usuário marque uma tarefa como concluída ou desfaça essa marcação.
- Pré-condições: A tarefa já existe.
- Pós-condições: A tarefa muda seu estado (concluída ou não).
- Fluxo principal:
- O usuário clica no botão “Concluir” ou “Desmarcar”.
- O sistema acessa a tarefa no dicionário do projeto.
- O método alternar_status() é chamado.
- O projeto é salvo com o novo estado da tarefa.
- A interface é atualizada com o novo status.

**Caso de Uso 3: Remover Tarefa**

- Ator principal: Usuário
- Objetivo: Permitir a exclusão permanente de uma tarefa do projeto.
- Pré-condições: A tarefa deve estar cadastrada.
- Pós-condições: A tarefa é excluída do sistema.
- Fluxo principal:
- O usuário clica no botão “Remover” ao lado de uma tarefa.
- O sistema identifica o título da tarefa.
- O método remover_tarefa() do projeto é chamado.
- A tarefa é removida do dicionário de tarefas.
- O projeto é salvo no banco de dados.
- A interface é atualizada, sem exibir a tarefa.

**Caso de Uso 4: Alternar Prioridade da Tarefa**

- Ator principal: Usuário
- Objetivo: Converter uma tarefa normal em importante e vice-versa.
- Pré-condições: A tarefa já deve existir.
- Pós-condições: A tarefa continua existindo, mas com tipo alterado.
- Fluxo principal:
- O usuário clica no botão “Prioridade” de uma tarefa.
- O sistema verifica se a tarefa é do tipo Tarefa ou TarefaImportante.
- Uma nova instância do tipo oposto é criada com os mesmos dados.
- A tarefa antiga é substituída no dicionário.
- O projeto é salvo.
- A interface exibe a tarefa como prioritária ou não.

**Caso de Uso 5: Visualizar Tarefas**

- Ator principal: Usuário
- Objetivo: Ver todas as tarefas cadastradas no projeto, com seus estados e prioridades.
- Pré-condições: O sistema precisa ter tarefas cadastradas.
- Pós-condições: Nenhuma alteração de dados ocorre.
- Fluxo principal:
- O usuário acessa a página inicial.
- O sistema carrega o projeto com suas tarefas do arquivo JSON.
- As tarefas são ordenadas (importantes primeiro).
- A interface exibe cada tarefa com seus botões e status visual.
