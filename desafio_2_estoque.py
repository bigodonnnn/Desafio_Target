# DESAFIO 2 - Controle de estoque

import time

estoque = [
    {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
    {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75},
    {"codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200},
    {"codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320},
    {"codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90}
]

def movimentar_estoque(codigo, quantidade, tipo, descricao):
    produto = next((p for p in estoque if p["codigoProduto"] == codigo), None)

    if not produto:
        print("❌ Produto não encontrado")
        return

    id_movimentacao = int(time.time() * 1000)

    if tipo == "entrada":
        produto["estoque"] += quantidade

    elif tipo == "saida":
        if produto["estoque"] < quantidade:
            print("❌ Estoque insuficiente")
            return
        produto["estoque"] -= quantidade

    else:
        print("❌ Tipo inválido")
        return

    print("\n✅ Movimentação realizada:")
    print({
        "ID": id_movimentacao,
        "Produto": produto["descricaoProduto"],
        "Tipo": tipo,
        "Descrição": descricao,
        "Quantidade": quantidade,
        "Estoque final": produto["estoque"]
    })


# TESTE
movimentar_estoque(101, 10, "saida", "Venda balcão")
