def registrar_notas ():    
    notas_lista = []
    while True:
        try:
            entrada = input("Digite a nota do aluno ou digite 'fim' para encerrar: ")
            if entrada == "fim":
                break # Interrompe o bloco de loop e segue o programa

            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_lista.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
                continue    
        except ValueError:
            print("Entrada inválida. Por favor digite um número ou 'fim'.")    

    if notas_lista:
        media = sum(notas_lista) / len(notas_lista)
        print(f"\nMédia da turma: {media:.2f}")
        print(f"Total de notas válidas é: {len(notas_lista)}")
    else:
        print("Nenhuma nota válida foi registrada.")

registrar_notas()            