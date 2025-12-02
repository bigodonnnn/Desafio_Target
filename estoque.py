import time

def buscar_produto(estoque, codigo):
    for produto in estoque:
        if produto["codigoProduto"] == codigo:
            return produto
    return None


def movimentar_estoque(estoque, codigo, quantidade, tipo, descricao):
    produto = buscar_produto(estoque, codigo)

    if not produto:
        raise ValueError("Produto não encontrado")

    if tipo == "saida" and produto["estoque"] < quantidade:
        raise ValueError("Estoque insuficiente")

    if tipo == "entrada":
        produto["estoque"] += quantidade
    elif tipo == "saida":
        produto["estoque"] -= quantidade
    else:
        raise ValueError("Tipo inválido")

    return {
        "id": int(time.time() * 1000),
        "produto": produto["descricaoProduto"],
        "tipo": tipo,
        "descricao": descricao,
        "quantidade": quantidade,
        "estoque_final": produto["estoque"]
    }


def main():
    estoque = [
        {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
        {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75}
    ]

    movimentacao = movimentar_estoque(
        estoque=estoque,
        codigo=101,
        quantidade=10,
        tipo="saida",
        descricao="Venda teste"
    )

    print(movimentacao)


if __name__ == "__main__":
    main()
