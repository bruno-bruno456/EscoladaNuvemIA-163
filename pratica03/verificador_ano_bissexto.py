"""
Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

Divisibilidade por 4: Se o ano é divisível por 4, é bissexto.
Exceção para múltiplos de 100: Se o ano é também múltiplo de 100, ele só é bissexto se também for múltiplo de 400.

"""
ano = int(input("Digite um número: "))

if ano % 4 == 0: # O ano pode ser bissexto
    if ano % 100 == 0: # Se o ano for divisível por 100, precisa ser analisado.
        if ano % 400 == 0: # Se o ano for também divisível por 400, então é bissexto.
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")   
    else:
        print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
