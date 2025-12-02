# Desafio Técnico – Target Sistemas (Python)

Este repositório contém a minha resolução para o desafio técnico proposto pela Target.
Optei por desenvolver tudo em Python, utilizando uma linguagem simples, organizada e fácil de entender.

Cada desafio possui suas próprias funções e uma função `main`, permitindo que sejam executados de forma independente.

---

## Organização do projeto

Os arquivos estão organizados de forma direta na raiz do projeto:

```
Desafio_Target/
├── comissao.py
├── estoque.py
├── juros.py
└── README.md
```

Cada arquivo representa um desafio diferente.

---

## Desafio 1 – Cálculo de Comissão (comissao.py)

Neste arquivo, a lógica calcula a comissão individual de cada venda e, em seguida, soma os valores por vendedor.

Regras aplicadas:

* Vendas abaixo de R$100,00: sem comissão
* Vendas entre R$100,00 e R$499,99: 1%
* Vendas a partir de R$500,00: 5%

Como executar:

```bash
python comissao.py
```

## Desafio 2 – Controle de Estoque (estoque.py)

Simula um sistema de controle de estoque com as seguintes funcionalidades:

* Busca de produto pelo código
* Entrada e saída de produtos
* Validação de quantidade disponível
* Registro de movimentação

Como executar:

```bash
python estoque.py
```

## Desafio 3 – Cálculo de Juros (juros.py)

Neste arquivo é feito o cálculo de juros baseado em atraso de pagamento.

Regra utilizada:

* Juros de 2,5% ao dia sobre o valor, considerando a diferença entre a data atual e a data de vencimento.

Como executar:

```bash
python juros.py
```

## Observações

O objetivo principal foi construir soluções claras, funcionais e organizadas, priorizando:

* Código limpo
* Boa legibilidade
* Organização lógica


---

## Autor

Brenner Fernandes
GitHub: [https://github.com/bigodonnnn](https://github.com/bigodonnnn)

Fico à disposição para esclarecimentos e explicações adicionais sobre a solução apresentada.
