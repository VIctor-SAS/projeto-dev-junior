print("Projeto Dev Junior v1")
print("Gerenciador de Tarefas no Terminal")


tarefa = []

def mostrar_menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1 - adicionar tarefa")
    print("2 - listar tarefa")
    print("3 - sair")

def adicionar_tarefa(lista_tarefas):
    tarefa = input("Digita a nova tarefa: ").strip()

    if tarefa == "":
        print('Tarefa invalida.')
    else:
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")

def listar_tarefa(lista_tarefa):
    if len(lista_tarefa) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        print("\nlista de tarefas")
        for i, tarefa in enumerate(lista_tarefa, start = 1):
            print(f"{i}. {tarefa}")


while True:
    mostrar_menu()
    opcao = input('Escolha uma opcao: ')

    if opcao == "1":
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        listar_tarefa(tarefa)
    elif opcao == "3":
        print("encerrando programa...")
        break

    else:
        print("Opcao invalida, tente novamente.")