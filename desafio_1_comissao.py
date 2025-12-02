# DESAFIO 1 - Cálculo de comissão

vendas = [
    {"vendedor": "João Silva", "valor": 1200.50},
    {"vendedor": "João Silva", "valor": 950.75},
    {"vendedor": "João Silva", "valor": 250.30},
    {"vendedor": "Maria Souza", "valor": 90.75},
    {"vendedor": "Maria Souza", "valor": 2100.40},
    {"vendedor": "Carlos Oliveira", "valor": 500.00},
    {"vendedor": "Carlos Oliveira", "valor": 125.75},
    {"vendedor": "Ana Lima", "valor": 75.30},
    {"vendedor": "Ana Lima", "valor": 1000.00}
]

def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05


comissoes = {}

for venda in vendas:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if vendedor not in comissoes:
        comissoes[vendedor] = 0

    comissoes[vendedor] += calcular_comissao(valor)


print("\n💰 COMISSÕES POR VENDEDOR:")
for vendedor, total in comissoes.items():
    print(f"{vendedor}: R$ {total:.2f}")
