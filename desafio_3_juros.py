# DESAFIO 3 - Cálculo de juros por atraso

from datetime import datetime

def calcular_juros(valor, data_vencimento):
    hoje = datetime.now()
    vencimento = datetime.strptime(data_vencimento, "%Y-%m-%d")

    if hoje <= vencimento:
        print("✅ Sem atraso. Juros = R$ 0,00")
        return 0

    dias = (hoje - vencimento).days
    juros = valor * 0.025 * dias

    print(f"⏳ Dias em atraso: {dias}")
    print(f"💰 Juros: R$ {juros:.2f}")

    return juros


# TESTE
calcular_juros(1000, "2025-11-01")
