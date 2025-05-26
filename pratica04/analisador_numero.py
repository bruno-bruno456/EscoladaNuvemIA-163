def analisador_numeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número intero ou 'fim' para encerrar: ")

        if entrada.lower() == "fim":
            break

        try:    
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                pares = pares + 1  # pares += 1
            else:
                print(f"O número {numero} é ímpar.")
                impares = impares + 1  # impares += 1
        except ValueError:
            print("Erro encontrado. Por favor, digite apenas números inteiros.")          
            continue


    print("\nResultado Final:")
    print(f"Quantidade de números pares é {pares}.")               
    print(f"Quantidade de números ímpares é {impares}.")               

analisador_numeros()    