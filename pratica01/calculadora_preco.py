"""
Calculadora de Preço Total
 Desenvolva um programa que calcula o preço total de uma compra. 
 Use as seguintes informações:
- Nome do produto: "Cadeira Infantil"
- Preço unitário: R$ 12.40
- Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, 
incluindo o resultado final
"""

# Calcular o preço total de uma compra

# Criação das variáveis
nome_produto = "Cadeira Infantil"
preco_unitario = 12.4
quantidade = 3

# Cálculo do preço total
preco_total = preco_unitario * quantidade

# Exibição dos valores
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")