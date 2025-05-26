def verifica_senha():
    while True:
        senha = input("Digite a senha (ou digite 'sair' para encerrar o programa): ")

        # Verificar se o usuário quer encerrar o programa.
        if senha == "sair":
            print("Programa encerrado.")
            break

        # Verificar comprimento da senha.    
        if len(senha) < 8:
            print("Senha fraca. A senha precisa ter pelo menos 8 caracteres.")
            continue

        # Verificar se a senha possúi um número.
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca. deve conter pelo menos um número.")
            continue

        # Verificar se a senha possúi um letra.
        if not any(caractere.isalpha() for caractere in senha):
            print("Senha fraca. deve conter pelo menos uma letra.")
            continue

        # Verificar se a senha possúi um letra.
        if not any(caractere.isupper() for caractere in senha):
            print("Senha fraca. deve conter pelo menos uma letra maiúscula.")
            continue

        # Se chegou até aqui, então a senha é válida
        print("Senha forte e válida.")
        break    




verifica_senha()
