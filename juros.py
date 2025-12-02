from datetime import datetime

def calcular_juros(valor, data_vencimento):
    hoje = datetime.now()
    vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")

    if hoje <= vencimento:
        return 0

    dias_atraso = (hoje - vencimento).days
    return valor * 0.025 * dias_atraso


def main():
    valor = 1000
    data_vencimento = "2025-11-01"

    juros = calcular_juros(valor, data_vencimento)

    print(f"Valor: R$ {valor}")
    print(f"Data de vencimento: {data_vencimento}")
    print(f"Juros: R$ {juros:.2f}")


if __name__ == "__main__":
    main()
