def main():
    print("--------------------- Bem-vindo a Loja de Roupas do Rogério Matos ------------------")
    print("-------------------------------------------Tabela de Roupas-----------------------------------------")
    print("-----------------------------------------------------------------------------------------------------")
    print("|                                             Modelo                                                |")
    print("|------------------------------|---------------------------------|----------------------------------|")
    print("| Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;             |")
    print("| Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos;              |")
    print("| Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos;      |")
    print("| Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos;        |")
    print("-----------------------------------------------------------------------------------------------------")
    
    #variaveis para armazenar os valores necessários para o calculo
    preco_unitario = escolha_modelo()
    quantidade = num_camisas()
    valor_frete = frete()

    # Aplicar desconto conforme quantidade
    desconto = 0
    if quantidade > 20000:
        print("Não aceitamos tantas camisas de uma vez.")
        return
    elif quantidade >= 2000:
        desconto = 0.12
    elif quantidade >= 200:
        desconto = 0.07
    elif quantidade >= 20:
        desconto = 0.05

    # Calcular valores
    valor_camisas = preco_unitario * quantidade
    valor_desconto = valor_camisas * desconto
    valor_total = valor_camisas - valor_desconto + valor_frete

    print(f"\nTotal do pedido:")
    print(f"Quantidade de camisas: {quantidade}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Valor total das camisas: R$ {valor_camisas:.2f}")
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Frete: R$ {valor_frete:.2f}")
    print(f"Valor total do pedido: R$ {valor_total:.2f}")

def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo (MCS, MLS, MCE, MLE): ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Opção inválida! Por favor, escolha entre MCS, MLS, MCE ou MLE.")

def num_camisas():
    while True:
        try:
            quantCamisas = int(input("Entre com o número de camisas: "))
            if quantCamisas <= 0:
                print("Por favor, entre com o número de camisas novamente.")
            elif quantCamisas > 20000:
                print("Não aceitamos tantas camisas de uma vez.")
            else:
                return quantCamisas
            
        except ValueError:
            print("Inválido! Por favor, insira um número inteiro.")

def frete():
    while True:
        print("\nEscolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100,00")
        print("2 - Frete por Sedex - R$ 200,00")
        print("0 - Retirar o pedido na fábrica - R$ 0,00")
        tipoFrete = input("Opção: ")
        if tipoFrete == "1":
            return 100.00
        elif tipoFrete == "2":
            return 200.00
        elif tipoFrete == "0":
            return 0.00
        else:
            print("Opção inválida! Por favor, escolha entre 1, 2 ou 0.")
# Iniciar o programa
main()