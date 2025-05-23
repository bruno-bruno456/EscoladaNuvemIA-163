""" (doc strings)
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo.

Use os seguintes dados:
- Distância percorrida: 300 km
- Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e 
exibir todos os dados da viagem, incluindo o resultado final 
arredondado para duas casas decimais.
"""

# Cálculadora de consumo de combustível

# Dados da viagem (comment strings)
distancia_percorrida = 300 # quilômetros (km)
combustivel_gasto = 25 # litros (l)

# Cálculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição dos dados
print("Dados da viagem") 
print(f"Distância percorrida: {distancia_percorrida} km") # (f strings)
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo:.2f} km/l")
