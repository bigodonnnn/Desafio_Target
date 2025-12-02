def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05


def calcular_comissoes(vendas):
    resultado = {}

    for venda in vendas:
        vendedor = venda['vendedor']
        valor = venda['valor']

        if vendedor not in resultado:
            resultado[vendedor] = 0

        resultado[vendedor] += calcular_comissao(valor)

    return resultado


def main():
    vendas = [
        {"vendedor": "João Silva", "valor": 1200.50},
        {"vendedor": "João Silva", "valor": 250.30},
        {"vendedor": "Maria Souza", "valor": 90.75},
        {"vendedor": "Carlos Oliveira", "valor": 500.00},
        {"vendedor": "Ana Lima", "valor": 1000.00}
    ]

    resultado = calcular_comissoes(vendas)

    for vendedor, total in resultado.items():
        print(f"{vendedor}: R$ {total:.2f}")


if __name__ == "__main__":
    main()
