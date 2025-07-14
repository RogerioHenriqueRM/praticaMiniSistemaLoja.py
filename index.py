# Loja do Rogério Matos - Cálculo de Parcelamento
def main():

    print("Bem-vindo a Loja do Rogério Matos")

    # Cliente passa o valor do produto e a quantidade de parcelas
    valor = float(input("Digite o valor do produto: "))
    quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

    # valor da taxa de juros
    taxaJuros = 0
    if quantidadeParcelas < 4:
        taxaJuros = 0/100
    elif quantidadeParcelas < 6:
        taxaJuros = 8/100
    elif quantidadeParcelas < 9:
        taxaJuros = 13/100
    elif quantidadeParcelas < 13:
        taxaJuros = 16/100
    else:
        taxaJuros = 32/100

    # Cálculo do valor total e valor da parcela
    valorTotal = valor * (1 + taxaJuros)
    valorParcela = valorTotal / quantidadeParcelas

    # valor total e valor da parcela que o cliente deve pagar
    print(f"O valor das parcelas é de:R$ {valorParcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valorTotal:.2f}")

main()
