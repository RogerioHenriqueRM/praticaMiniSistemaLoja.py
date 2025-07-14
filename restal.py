
def main():
    #variável para armazenar o valor total
    total = 0
    # Loop para permitir múltiplos pedidos
    while True:
        print("--- Bem-vindo a Loja de Marmitas do Rogério Matos ---")
        print("----------------------Cardápio-----------------------")
        print("-----------------------------------------------------")
        print("| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |")
        print("|---------|--------------------|--------------------|")
        print("|    P    |      R$ 16.00      |      R$ 15.00      |")
        print("|    M    |      R$ 18.00      |      R$ 17.00      |")
        print("|    G    |      R$ 22.00      |      R$ 21.00      |")
        print("-----------------------------------------------------")

        # sabor e tamanho desejados
        #condição para verificar se o sabor e tamanho são válidos
        saborDesejado = input("Entre com o sabor desejado (BA/FF): ")
        if saborDesejado not in ['BA', 'FF']:
            print("Sabor inválido. Por favor, tente novamente.")
            continue

        tamanhoDesejado = input("Entre com o tamanho desejado (P/M/G): ")
        if tamanhoDesejado not in ['P', 'M', 'G']:
            print("Tamanho inválido. Por favor, tente novamente.")
            continue
        # Cálculo do valor da marmita
        if saborDesejado == 'BA':
            if tamanhoDesejado == 'P':
                valor = 16.00
            elif tamanhoDesejado == 'M':
                valor = 18.00
            else:
                valor = 22.00
        else:
            if tamanhoDesejado == 'P':
                valor = 15.00
            elif tamanhoDesejado == 'M':
                valor = 17.00
            else:
                valor = 21.00

        total += valor
        print(f"O valor da sua marmita é: R$ {valor:.2f}")

        #loop para verificar se o cliente deseja adicionar mais marmitas

        repetir = input("Deseja fazer outro pedido? (S/N): ").strip().upper()
        if repetir != 'S':
            print("Obrigado por escolher a Loja de Marmitas do Rogério Matos")
            print(f"O total dos seus pedidos foi: R$ {total:.2f}")
            break

main()
