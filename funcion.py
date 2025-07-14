# EXIGÊNCIA DE CÓDIGO 1 de 8
print("Bem-vindo a empresa do Rogério Matos")

# Lista para armazenar os funcionários cadastrados junto com um ID global para controle
lista_funcionarios = []
id_global = 12345678  

# função para cadastrar funcionário
def cadastrar_funcionario(id_atual):
    
    print("\n--- Cadastro de Funcionário ---")
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    try:
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Salário inválido. Cadastro cancelado.")
        return

    funcionario = {
        "id": id_atual,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!\n")

#função para consultar funcionários
def consultar_funcionarios():
    """Função para consultar funcionários"""
    while True:
        print("\n--- Consulta de Funcionários ---")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao Menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Lista de Todos os Funcionários ---")
            for func in lista_funcionarios:
                print(func)
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
                encontrado = False
                for func in lista_funcionarios:
                    if func["id"] == id_busca:
                        print(func)
                        encontrado = True
                if not encontrado:
                    print("Funcionário com esse ID não encontrado.")
            except ValueError:
                print("ID inválido.")
        elif opcao == "3":
            setor_busca = input("Digite o setor para consulta: ")
            encontrados = [func for func in lista_funcionarios if func["setor"].lower() == setor_busca.lower()]
            if encontrados:
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4":
            return  # Volta ao menu principal
        else:
            print("Opção inválida.")

# função para remover funcionário
def remover_funcionario():
    """Função para remover funcionário por ID"""
    while True:
        try:
            id_remove = int(input("\nDigite o ID do funcionário que deseja remover: "))
            removido = False
            for func in lista_funcionarios:
                if func["id"] == id_remove: # Verifica o ID do funcionario pra remover ele em seguida 
                    lista_funcionarios.remove(func)
                    print("Funcionário removido com sucesso.")
                    removido = True
                    break
            if not removido:
                print("ID inválido.")
            else:
                break
        except ValueError:
            print("ID inválido. Tente novamente.")


# Menu principal
while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    escolha = input("Escolha uma opção: ")

    #condições para verificar a opção escolhida
    if escolha == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif escolha == "2":
        consultar_funcionarios()
    elif escolha == "3":
        remover_funcionario()
    elif escolha == "4":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
