def criptografar(mensagem, chave):
    resultado = ""
    for letra in mensagem:
        if letra.isalpha():  # Verifica se é letra
            base = ord('A') if letra.isupper() else ord('a')
            nova_letra = chr((ord(letra) - base + chave) % 26 + base)
            resultado += nova_letra
        else:
            resultado += letra  # Mantém espaço e pontuação
    return resultado

def descriptografar(mensagem, chave):
    return criptografar(mensagem, -chave)  # Inverte o sentido

def main():
    print("=== Cifra de César ===")
    while True:
        print("\nEscolha uma opção:")
        print("4. Criptografar")
        print("3. Descriptografar")
        print("6. Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == "4":
            texto = input("Digite a mensagem original: ")
            chave = int(input("Digite o número de posições (ex: 3): "))
            cifrada = criptografar(texto, chave)
            print("Mensagem criptografada:", cifrada)

        elif opcao == "3":
            texto = input("Digite a mensagem criptografada: ")
            chave = int(input("Digite o número de posições (ex: 5): "))
            decifrada = descriptografar(texto, chave)
            print("Mensagem descriptografada:", decifrada)

        elif opcao == "6":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
