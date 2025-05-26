
"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre 
Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, 
a unidade de origem e 
a unidade para qual deseja converter.


De Celsius para Fahrenheit: F = (C * 9/5) + 32
De Fahrenheit para Celsius: C = (F - 32) * 5/9
De Celsius para Kelvin: K = C + 273,15
De Kelvin para Celsius: C = K - 273,15
De Fahrenheit para Kelvin: K = (F - 32) * 5/9 + 273,15
De Kelvin para Fahrenheit: F = (K - 273,15) * 9/5 + 32

"""

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a temperatura de origem (C, F ou K): ").upper()
destino = input("Digite a temperatura de destino (C, F ou K): ").upper()


if origem == destino:
    resultado = temperatura
elif origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    else:
        resultado = temperatura + 273.15   
elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    else:
        resultado = (temperatura - 32) * 5/9 + 273.15
else:
    if destino == "C":
        resultado = temperatura - 273.15
    else:
        resultado = (temperatura - 273.15) * 9/5 + 32


print(f"A temperatura {temperatura} {origem} é igual a {resultado} {destino}")